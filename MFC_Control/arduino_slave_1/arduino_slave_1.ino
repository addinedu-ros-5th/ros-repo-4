#include <Wire.h>
#include <Servo.h>
#include <Keypad.h>

#define LED_PIN 2
#define SLAVE_ADDRESS 0x08  // 슬레이브 보드 주소 (I2C 통신)

Servo servo1; //상품코드 

String productCode = ""; // 완료된 품번 정보를 저장할 변수
int expectedQuantity = 0; // 예상 수량을 저장할 변수
int enteredQuantity = 0; // 입력된 수량을 저장할 변수
bool inspectionComplete = false;
unsigned long startMillis = 0;  // 서보 모터가 회전한 시각 저장
bool servoMoved = false; // 서보 모터 상태 추적
bool waitingForKeypadInput = false; // 키패드 입력 대기 상태 추적

const byte ROWS = 4; // 키패드의 행 수
const byte COLS = 4; // 키패드의 열 수

char keys[ROWS][COLS] = {
  {'1', '2', '3', 'A'},
  {'4', '5', '6', 'B'},
  {'7', '8', '9', 'C'},
  {'*', '0', '#', 'D'}
};

byte rowPins[ROWS] = {9, 8, 7, 6}; // 행 핀
byte colPins[COLS] = {5, 4, 3, 2}; // 열 핀

Keypad keypad = Keypad(makeKeymap(keys), rowPins, colPins, ROWS, COLS);
String enteredCode = ""; // 키패드로 입력된 값을 저장할 변수
String enteredQuantityStr = ""; // 키패드로 입력된 수량을 저장할 변수

bool enteringCode = true; // 코드 입력 상태 추적

void setup() {
  Serial.begin(9600); // 시리얼 모니터 시작
  pinMode(LED_PIN, OUTPUT);
  Wire.begin(SLAVE_ADDRESS); // I2C 슬레이브 주소 설정
  Wire.onReceive(receiveEvent); // 데이터 수신 핸들러 설정
  Wire.onRequest(requestEvent); // 데이터 요청 핸들러 설정

  // 서보 모터 핀 설정
  servo1.attach(13); // 서보 모터 1 핀

  // 서보 모터 초기 위치 설정
  servo1.write(180);

  pinMode(A4, INPUT_PULLUP); // SDA에 내장 풀업 저항 활성화
  pinMode(A5, INPUT_PULLUP); // SCL에 내장 풀업 저항 활성화

  Serial.println("Arduino ready as I2C slave with address 0x08");
}

void loop() {
  char key = keypad.getKey();
  if (key && waitingForKeypadInput) {
    handleKeypadInput(key);
  }
}

void handleKeypadInput(char key) {
  if (key >= '0' && key <= '9') {
    if (enteringCode) {
      enteredCode += key;
      Serial.print("Entered code: ");
      Serial.println(enteredCode);
      Serial.println("Enter the next digit or press # to confirm the code.");
    } else {
      enteredQuantityStr += key;
      Serial.print("Entered quantity: ");
      Serial.println(enteredQuantityStr);
      Serial.println("Enter the next digit or press # to confirm the quantity.");
    }
  } else if (key == '#') { // 입력 완료 확인
    if (enteringCode) {
      Serial.print("Entered code to compare: ");
      Serial.println(enteredCode);
      enteringCode = false; // 수량 입력 상태로 전환
      Serial.println("Enter the quantity now, followed by # to confirm.");
    } else {
      enteredQuantity = enteredQuantityStr.toInt();
      Serial.print("Entered quantity to compare: ");
      Serial.println(enteredQuantity);

      if (enteredCode == productCode.substring(1, 3) && enteredQuantity == expectedQuantity) { // 제품 코드의 두 자리 숫자와 비교 및 수량 비교
        servo1.write(0); // 일치하면 서보 모터를 0도로 이동
        Serial.println("Code and quantity matched, servo moved to 0 degrees for product: " + productCode);

        inspectionComplete = true; // 검수 완료로 설정

        waitingForKeypadInput = false; // 키패드 입력 대기 상태 종료
        enteredCode = ""; // 입력 코드 초기화
        enteredQuantityStr = ""; // 입력 수량 초기화
        enteringCode = true; // 코드 입력 상태로 전환
      } else {
        Serial.println("Code or quantity did not match. Please try again.");
        enteredCode = ""; // 입력 코드 초기화
        enteredQuantityStr = ""; // 입력 수량 초기화
        enteringCode = true; // 코드 입력 상태로 전환
        Serial.println("Enter the product code again, followed by # to confirm.");
      }
    }
  } else if (key == '*') { // 입력 초기화
    if (enteringCode) {
      enteredCode = "";
      Serial.println("Input code cleared. Enter the code again.");
    } else {
      enteredQuantityStr = "";
      Serial.println("Input quantity cleared. Enter the quantity again.");
    }
  }
}

void receiveEvent(int howMany) {
  String command = "";
  while (Wire.available()) {
    char c = Wire.read();
    if (c != '\r' && c != '\n' && c != '\0') { // 개행 문자와 널 문자를 제거
      command += c;
    }
  }
  Serial.print("Received command: ");
  Serial.println(command);
  
  if (command.startsWith("START_INSPECTION:")) {
    int firstSeparator = command.indexOf(':');
    int secondSeparator = command.indexOf(':', firstSeparator + 1);
    
    if (firstSeparator != -1 && secondSeparator != -1) {
      productCode = command.substring(firstSeparator + 1, secondSeparator);
      expectedQuantity = command.substring(secondSeparator + 1).toInt();

      // 서보 모터를 180도로 회전
      servo1.write(180);
      waitingForKeypadInput = true; // 키패드 입력 대기 상태 설정

      Serial.println("Start inspection for product: " + productCode + " with expected quantity: " + expectedQuantity);
      Serial.println("Servo moved to 180 degrees for product: " + productCode);
      Serial.println("Enter the product code, followed by # to confirm.");
    } else {
      Serial.println("Invalid command format.");
    }
  } else {
    Serial.println("Unknown command.");
  }
}

void requestEvent() {
  if (inspectionComplete) {
    String completionMessage = "INSPECTION_COMPLETE:" + productCode;
    Wire.write(completionMessage.c_str(), completionMessage.length() + 1);
    inspectionComplete = false; // 메시지 전송 후 상태 초기화
    Serial.println("Sent inspection complete signal to master with product: " + productCode);
  }
}
