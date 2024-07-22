#include <Wire.h>

#define LED_PIN 2

void setup() {
  Serial.begin(9600); // 시리얼 모니터 시작
  pinMode(LED_PIN, OUTPUT);
  Wire.begin(0x09); // I2C 슬레이브 주소 설정
  Wire.onReceive(receiveEvent);
  pinMode(A4, INPUT_PULLUP); // SDA에 내장 풀업 저항 활성화
  pinMode(A5, INPUT_PULLUP); // SCL에 내장 풀업 저항 활성화

  Serial.println("Arduino ready as I2C slave with address 0x08");
}

void loop() {
  // 메인 루프가 필요하지 않음
}

void receiveEvent(int howMany) {
  String command = "";
  while (Wire.available()) {
    char c = Wire.read();
    command += c;
  }

  Serial.print("Received command: ");
  Serial.println(command);
  
  if (command == "LED_ON") {
    digitalWrite(LED_PIN, HIGH); // LED 켜기
    Serial.println("LED turned ON");
  } else {
    Serial.println("Unknown command");
  }
}
