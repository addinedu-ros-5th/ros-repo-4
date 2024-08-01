#include <Wire.h>
#include <Servo.h>
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
    movingServo2To0=true;
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
