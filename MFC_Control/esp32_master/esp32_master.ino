#include <WiFi.h>
#include <Wire.h>
#include <WiFiClient.h>
#include <WiFiServer.h>

const char* ssid = "addinedu_class_1(2.4G)";
const char* password = "addinedu1";

#define SLAVE1_ADDR 0x08
#define SLAVE2_ADDR 0x09

WiFiServer server(80); // TCP 서버 포트 설정

unsigned long previousMillis = 0; // 이전 시간 저장
const long interval = 1000; // 1초 간격

String MFCNetworkManagerIP = "192.168.2.28"; // network_manager IP 주소
const uint16_t networkManagerPort = 12345;

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
  handleClientRequest();
  checkInspectionComplete();
}

void handleClientRequest() {
  WiFiClient client = server.available(); // 클라이언트 접속 대기

  if (client) {
    Serial.println("Client connected");
    while (client.connected()) {
      if (client.available()) {
        String request = client.readStringUntil('\n');
        Serial.println("Received request: " + request);
        if (request.startsWith("START_INSPECTION:")) {
          String productCode = request.substring(request.indexOf(':') + 1);
          Serial.println("Received start inspection signal for product: " + productCode);
          sendCommandToArduino(SLAVE1_ADDR, "LED_ON:" + productCode);
          sendCommandToArduino(SLAVE2_ADDR, "LED_ON:" + productCode);

          client.println("Inspection started for product: " + productCode);
        }
        // 다른 요청을 처리하기 위한 조건문을 추가하세요.
      }
    }
    client.stop();
    Serial.println("Client disconnected");
  }
}

void checkInspectionComplete() {
  unsigned long currentMillis = millis();
  if (currentMillis - previousMillis >= interval) {
    previousMillis = currentMillis;

    // 슬레이브로부터 검사 완료 데이터를 요청
    requestInspectionComplete(SLAVE1_ADDR);
    requestInspectionComplete(SLAVE2_ADDR);
  }
}

void sendCommandToArduino(uint8_t address, String command) {
  Wire.beginTransmission(address);
  Wire.write((const uint8_t*)command.c_str(), command.length() + 1); // null terminator 포함
  Wire.endTransmission();
}


void requestInspectionComplete(uint8_t address) {
  Wire.requestFrom(address, 33); // null terminator 포함 33 바이트의 데이터를 요청 (예: 최대 메시지 길이)
  char response[33] = {0}; // 버퍼 초기화
  int i = 0;
  while (Wire.available()) {
    char c = Wire.read();
    if (i < 32) {
      response[i++] = c;
    }
  }
  response[i] = '\0'; // null terminator 추가

  String responseStr = String(response);
  if (responseStr.startsWith("INSPECTION_COMPLETE:")) {
    String productCode = responseStr.substring(responseStr.indexOf(':') + 1);
    Serial.println("Inspection completed for product: " + productCode);
    // 필요한 추가 작업 수행
    notifyNetworkManager(productCode);
  }
}

void notifyNetworkManager(const String& productCode) {
  WiFiClient client;
  Serial.println("Attempting to connect to network manager...");
  if (client.connect(MFCNetworkManagerIP.c_str(), networkManagerPort)) {
    String message = "TASK_COMPLETE:" + productCode;
    client.print(message);
    client.stop();
    Serial.println("Sent task completion to network_manager: " + message);
  } else {
    Serial.println("Connection to network_manager failed");
  }
}