#include <WiFi.h>

// const char* ssid = "addinedu_class_1(2.4G)";
// const char* password = "addinedu1";

const char* ssid = "Tmwlakfk_>u<";
const char* password = "96989898";

WiFiServer server(80); // TCP 서버 포트 설정

// 18개의 LED 핀 설정
const int LED_PINS[] = {4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21}; 

void setup() {
  Serial.begin(9600);

  // 모든 LED 핀을 출력으로 설정
  for (int i = 0; i < 18; i++) {
    pinMode(LED_PINS[i], OUTPUT);
    digitalWrite(LED_PINS[i], LOW); // 초기 상태는 OFF
  }

  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }

  Serial.println("Connected to WiFi");
  Serial.print("Slave IP address: ");
  Serial.println(WiFi.localIP()); // 슬레이브 IP 주소 출력

  server.begin();
}

void loop() {
  WiFiClient client = server.available();

  if (client) {
    Serial.println("Client connected");
    while (client.connected()) {
      if (client.available()) {
        String request = client.readStringUntil('\n');
        request.trim();
        
        Serial.println("Received request: " + request);

        // 요청에 따라 LED 제어
        if (request.startsWith("R_")) {
          int ledIndex = getLedIndex(request);
          if (ledIndex != -1) {
            digitalWrite(LED_PINS[ledIndex], HIGH); // LED 켜기
            Serial.println("LED turned ON for rack: " + request);
            delay(5000); // 5초 대기
            digitalWrite(LED_PINS[ledIndex], LOW); // LED 끄기
            Serial.println("LED turned OFF for rack: " + request);
          }
        }
      }
    }
    client.stop();
    Serial.println("Client disconnected");
  }
}

// 요청에 따른 LED 인덱스 반환 함수
int getLedIndex(String rack) {
  if (rack == "R_A1") return 0;
  if (rack == "R_A2") return 1;
  if (rack == "R_A3") return 2;
  if (rack == "R_B1") return 3;
  if (rack == "R_B2") return 4;
  if (rack == "R_B3") return 5;
  if (rack == "R_C1") return 6;
  if (rack == "R_C2") return 7;
  if (rack == "R_C3") return 8;
  if (rack == "R_D1") return 9;
  if (rack == "R_D2") return 10;
  if (rack == "R_D3") return 11;
  if (rack == "R_E1") return 12;
  if (rack == "R_E2") return 13;
  if (rack == "R_E3") return 14;
  if (rack == "R_F1") return 15;
  if (rack == "R_F2") return 16;
  if (rack == "R_F3") return 17;
  return -1; // 잘못된 요청
}
