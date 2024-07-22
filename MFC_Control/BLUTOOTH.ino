#include <SoftwareSerial.h>

SoftwareSerial BTSerial(4, 3); // RX, TX
const int ledPin = 13;  // LED가 연결된 핀 번호

void setup() {
  pinMode(ledPin, OUTPUT);  // LED 핀을 출력으로 설정
  Serial.begin(9600);
  BTSerial.begin(9600);
  Serial.println("Ready to pair with HC-06");
}

void loop() {
  if (BTSerial.available()) {
    String data = BTSerial.readStringUntil('\n');
    Serial.print("Received from BT: ");
    Serial.println(data);

    // 수신된 데이터에 따라 LED 제어
    if (data == "1") {
      digitalWrite(ledPin, HIGH);  // LED 켜기
      Serial.println("LED ON");
    } else if (data == "2") {
      digitalWrite(ledPin, LOW);   // LED 끄기1
      Serial.println("LED OFF");
    }
  }

  if (Serial.available()) {
    String data = Serial.readStringUntil('\n');
    BTSerial.println(data);
    Serial.print("Sent to BT: ");
    Serial.println(data);
  }
}