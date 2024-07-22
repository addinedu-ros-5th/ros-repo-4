#include <WiFi.h>

const char* ssid = "addinedu_class_2 (2.4G)";
const char* password = "addinedu1";
WiFiServer server(80); // TCP 서버 포트 설정
void setup() {
  Serial.begin(9600);

  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }
  Serial.println("Connected to WiFi");
  Serial.println("IP address: ");
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
          client.println("Inspection started");
        }
      }
    }
    client.stop();
    Serial.println("Client disconnected");
  }
}