#include <Wire.h>

#define LED_PIN 2
#define SLAVE_ADDRESS 0x08  // 슬레이브 보드 주소 (I2C 통신)

String productCode = ""; // 완료된 품번 정보를 저장할 변수
bool inspectionComplete = false;
unsigned long startMillis = 0;  // LED 켜진 시각 저장
bool ledOn = false; // LED 상태 추적

void setup() {
  Serial.begin(9600); // 시리얼 모니터 시작
  pinMode(LED_PIN, OUTPUT);
  Wire.begin(SLAVE_ADDRESS); // I2C 슬레이브 주소 설정
  Wire.onReceive(receiveEvent); // 데이터 수신 핸들러 설정
  Wire.onRequest(requestEvent); // 데이터 요청 핸들러 설정
  pinMode(A4, INPUT_PULLUP); // SDA에 내장 풀업 저항 활성화
  pinMode(A5, INPUT_PULLUP); // SCL에 내장 풀업 저항 활성화

  Serial.println("Arduino ready as I2C slave with address 0x08");
}

void loop() {
  // 3초 대기 후 LED를 끄고 검사 완료 플래그 설정
  if (ledOn && (millis() - startMillis >= 3000)) {
    digitalWrite(LED_PIN, LOW); // LED 끄기
    ledOn = false;
    inspectionComplete = true;
    Serial.println("LED turned OFF for product: " + productCode);
  }
}

void receiveEvent(int howMany) {
  String command = "";
  while (Wire.available()) {
    char c = Wire.read();
    command += c;
  }

  Serial.print("Received command: ");
  Serial.println(command);
  
  if (command.startsWith("LED_ON")) {
    int separatorIndex = command.indexOf(':');
    if (separatorIndex != -1) {
      productCode = command.substring(separatorIndex + 1);
      digitalWrite(LED_PIN, HIGH); // LED 켜기
      startMillis = millis(); // 현재 시각 저장
      ledOn = true;
      Serial.println("LED turned ON for product: " + productCode);
    } else {
      Serial.println("Invalid command format");
    }
  } else {
    Serial.println("Unknown command");
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
