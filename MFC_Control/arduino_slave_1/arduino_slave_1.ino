#include <Wire.h>
#include <Servo.h>

// 7-segment 디스플레이 제어를 위한 핀 정의
#define SEG_A 2
#define SEG_B 3
#define SEG_C 4
#define SEG_D 5
#define SEG_E 6
#define SEG_F 7
#define SEG_G 8
#define SEG_DP 9

#define SLAVE_ADDRESS 0x08  // 슬레이브 보드 주소 (I2C 통신)

Servo servo1; // 상품코드
Servo servo2; // 상품수량

String productCode = ""; // 완료된 품번 정보를 저장할 변수
int expectedQuantity = 0; // 예상 수량을 저장할 변수

bool inspectionComplete = false;
bool productCodeInspection = false;
bool quantityInspection = false;

int percentage = 100; // 검수 통과 확률
unsigned long servoMoveStartTime = 0; // 서보 모터가 회전한 시각 저장
bool movingServo1To0 = false;
bool movingServo2To0 = false;
bool servo1At180 = false; // 서보1이 180도에 도달했는지 여부
bool servo2At180 = false; // 서보2가 180도에 도달했는지 여부

int inspectedCount = 0; // 검수 완료된 개수

byte segmentDigits[] = {
  0b00111111, // 0
  0b00000110, // 1
  0b01011011, // 2
  0b01001111, // 3
  0b01100110, // 4
  0b01101101, // 5
  0b01111101, // 6
  0b00000111, // 7
  0b01111111, // 8
  0b01101111  // 9
};

void setup() {
  Serial.begin(9600); // 시리얼 모니터 시작
  Wire.begin(SLAVE_ADDRESS); // I2C 슬레이브 주소 설정
  Wire.onReceive(receiveEvent); // 데이터 수신 핸들러 설정
  Wire.onRequest(requestEvent); // 데이터 요청 핸들러 설정

  // 서보 모터 핀 설정
  servo1.attach(13); // 서보 모터 1 핀
  servo2.attach(11); // 서보 모터 2 핀
  // 서보 모터 초기 위치 설정
  servo1.write(0);
  servo2.write(0);

  pinMode(A4, INPUT_PULLUP); // SDA에 내장 풀업 저항 활성화
  pinMode(A5, INPUT_PULLUP); // SCL에 내장 풀업 저항 활성화

  Serial.println("Arduino ready as I2C slave with address 0x08");

  // 7-segment 디스플레이 제어 핀 설정
  pinMode(SEG_A, OUTPUT);
  pinMode(SEG_B, OUTPUT);
  pinMode(SEG_C, OUTPUT);
  pinMode(SEG_D, OUTPUT);
  pinMode(SEG_E, OUTPUT);
  pinMode(SEG_F, OUTPUT);
  pinMode(SEG_G, OUTPUT);
  pinMode(SEG_DP, OUTPUT);

  // 초기 디스플레이 값 설정
  updateDisplay(inspectedCount);
}

void loop() {
  unsigned long currentMillis = millis();

  // 서보 모터 1이 180도에서 0도로 이동
  if (movingServo1To0) {
    if (currentMillis - servoMoveStartTime >= 3000) { // 3초 대기 후 이동
      servo1.write(0);
      movingServo1To0 = false;
      Serial.println("Servo 1 moved to 0 degrees");
      Serial.println("Product Code Inspection passed");
      productCodeInspection = false;
      quantityInspection = true;  // 다음 단계로 이동
      servoMoveStartTime = currentMillis;  // 타이머 초기화
    }
  }

  // 서보 모터 2가 180도에서 0도로 이동
  if (movingServo2To0) {
    if (currentMillis - servoMoveStartTime >= 3000) { // 3초 대기 후 이동
      servo2.write(0);
      movingServo2To0 = false;
      Serial.println("Servo 2 moved to 0 degrees");
      quantityInspection = false;
      inspectionComplete = true;
      inspectedCount++;  // 검수 완료된 개수 증가
      updateDisplay(inspectedCount);  // 7-segment 디스플레이 업데이트
    }
  }

  // 검수 플래그에 따라 서보 모터 이동 시작
  if (productCodeInspection && !servo1At180) {
    servo1.write(180);
    movingServo1To0 = true;
    servo1At180 = true;
    servoMoveStartTime = millis();
  }
  if (quantityInspection && !servo2At180) {
    servo2.write(180);
    servo2At180 = true;
    movingServo2To0 = true;
    servoMoveStartTime = millis();
  }
}

void handleInspection() {
  int randomValue = random(100); // 0에서 99 사이의 랜덤 값 생성
  if (randomValue < percentage) {
    productCodeInspection = true;
    servo1At180 = false; // 플래그 초기화
    servo2At180 = false; // 플래그 초기화
    Serial.println("Starting inspections...");
  } else {
    Serial.println("Inspection failed.");
    inspectionComplete = false; // 검수 실패로 설정
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

      // 서보 모터를 초기 위치로 회전

      Serial.println("Start inspection for product: " + productCode + " with expected quantity: " + expectedQuantity);
      Serial.println("Servo moved to 0 degrees for product: " + productCode);

      // 검수 처리 호출
      handleInspection();
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

void updateDisplay(int number) {
  // 0-9 범위 안의 숫자만 표시
  if (number < 0 || number > 9) return;

  byte segments = segmentDigits[number];

  digitalWrite(SEG_A, segments & 0b00000001);
  digitalWrite(SEG_B, segments & 0b00000010);
  digitalWrite(SEG_C, segments & 0b00000100);
  digitalWrite(SEG_D, segments & 0b00001000);
  digitalWrite(SEG_E, segments & 0b00010000);
  digitalWrite(SEG_F, segments & 0b00100000);
  digitalWrite(SEG_G, segments & 0b01000000);
  digitalWrite(SEG_DP, segments & 0b10000000);
}
