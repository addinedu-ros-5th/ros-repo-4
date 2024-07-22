#include <WiFi.h>
#include <Wire.h>

const char* ssid = "addinedu_class_2 (2.4G)";
const char* password = "addinedu1";

#define SLAVE1_ADDR 0x08
#define SLAVE2_ADDR 0x09

WiFiServer server(80); // TCP 서버 포트 설정

void setup() {
  Serial.begin(9600);

  // I2C 핀에 대해 내장 풀업 저항 활성화
  pinMode(21, INPUT_PULLUP); // SDA
  pinMode(22, INPUT_PULLUP); // SCL

  Wire.begin(21, 22); // I2C 마스터 초기화, SDA=GPIO 21, SCL=GPIO 22

  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }

  Serial.println("Connected to WiFi");
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());

  server.begin(); // TCP 서버 시작
}

void loop() {
  WiFiClient client = server.available(); // 클라이언트 접속 대기

  if (client) {
    Serial.println("Client connected");
    while (client.connected()) {
      if (client.available()) {
        String request = client.readStringUntil('\n');
        Serial.println("Received request: " + request);
        if (request == "START_INSPECTION") {
          Serial.println("Received start inspection signal");
          sendCommandToArduino(SLAVE1_ADDR, "LED_ON");
          sendCommandToArduino(SLAVE2_ADDR, "LED_ON");


          // Wi-Fi로 ESP32 슬레이브 보드에 명령 전송
          WiFiClient espClient;
          if (espClient.connect("192.168.0.14", 80)) { // 슬레이브 보드 IP 주소
            espClient.println("LED_ON");
            espClient.stop();
          }
          
          client.println("Inspection started");
        }
      }
    }
    client.stop();
    Serial.println("Client disconnected");
  }
}

void sendCommandToArduino(uint8_t address, String command) {
  Wire.beginTransmission(address);
  Wire.write((const uint8_t*)command.c_str(), command.length());
  Wire.endTransmission();
}
