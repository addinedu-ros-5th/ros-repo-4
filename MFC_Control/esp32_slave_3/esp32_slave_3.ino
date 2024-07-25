#include <WiFi.h>

const char* ssid = "addinedu_class_2 (2.4G)";
const char* password = "addinedu1";

WiFiServer server(80); // TCP 서버 포트 설정

#define LED_PIN 4

void setup() {
  Serial.begin(9600);
  pinMode(LED_PIN, OUTPUT);

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
        
        if (request == "LED_ON") {
          digitalWrite(LED_PIN, HIGH); // LED 켜기
          Serial.println("LED turned ON");
        }
      }
    }
    client.stop();
    Serial.println("Client disconnected");
  }
}
