#include <WiFi.h>
#include <Wire.h>
#include <WiFiClient.h>
#include <WiFiServer.h>

// const char* ssid = "TOM N TOMS 2G";

// const char* ssid = "902";
// const char* password = "22177070";

// const char* ssid = "addinedu_class_1(2.4G)";
// const char* password = "addinedu1";

// const char* ssid = "김미꾜";
// const char* password = "01033616648";

// const char* ssid = "CLL5G";
// const char* password = "cll16661140";


const char* ssid = "Tmwlakfk_>u<";
const char* password = "96989898";

// const char* ssid = "FOREST_GB_2G";
// const char* password = "forest1234";


#define SLAVE1_ADDR 0x08
#define SLAVE2_ADDR 0x09

WiFiServer server(80); // TCP 서버 포트 설정

unsigned long previousMillis = 0; // 이전 시간 저장
const long interval = 1000; // 1초 간격

// String MFCNetworkManagerIP = "172.30.1.28"; // network_manager IP 주소 탐탐
// String MFCNetworkManagerIP = "192.168.0.15"; // network_manager IP 주소 쬰지네
// String MFCNetworkManagerIP = "192.168.2.28"; // network_manager IP 주소 학원172.20.10.8

// String MFCNetworkManagerIP = "172.20.10.8"; // network_manager IP 주소 학원
String MFCNetworkManagerIP = "192.168.1.104"; // network_manager IP 주소 학원>3<

// String MFCNetworkManagerIP = "192.168.0.11"; // network_manager IP 주소 개방~
const uint16_t networkManagerPort = 12345;


// String slave3IP = "192.168.2.84"; // 슬레이브 3 IP 주소(ESP32 RACK LED) 학원
String slave3IP = "192.168.1.106"; // 슬레이브 3 IP 주소(ESP32 RACK LED) >ㅁ<

// String slave3IP = "192.168.0.15"; // 슬레이브 3 IP 주소(ESP32 RACK LED)개방
const uint16_t slave3Port = 80; // 슬레이브 보드의 서버 포트

void setup() {
  Serial.begin(9600);

  // I2C 핀에 대해 내장 풀업 저항 활성화
  pinMode(21, INPUT_PULLUP); // SDA
  pinMode(22, INPUT_PULLUP); // SCL

  Wire.begin(21, 22); // I2C 마스터 초기화, SDA=GPIO 21, SCL=GPIO 22

  WiFi.begin(ssid, password);
  // WiFi.begin(ssid);
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
          int firstSeparator = request.indexOf(':');
          int secondSeparator = request.indexOf(':', firstSeparator + 1);
          
          if (firstSeparator != -1 && secondSeparator != -1) {
            String productCode = request.substring(firstSeparator + 1, secondSeparator);
            String quantity = request.substring(secondSeparator + 1);
            Serial.println("Received start inspection signal for product: " + productCode + " with quantity: " + quantity);
            sendCommandToArduino(SLAVE1_ADDR, "START_INSPECTION:" + productCode + ":" + quantity);
            // sendCommandToArduino(SLAVE2_ADDR, "START_INSPECTION:" + productCode + ":" + quantity);

            client.println("Inspection started for product: " + productCode + " with quantity: " + quantity);
          }
        }
        
        if (request.startsWith("START-입고:")) {
          int firstSeparator = request.indexOf('[');
          int secondSeparator = request.indexOf(']', firstSeparator + 1);
          
          if (firstSeparator != -1 && secondSeparator != -1) {
            String rackList = request.substring(firstSeparator + 1, secondSeparator);
            rackList.trim();
            Serial.println("Received rack list: " + rackList);
            rackList.replace("'", ""); // 따옴표 제거
            sendCommandToSlave(slave3IP, rackList);

            client.println("Inspection started for racks: " + rackList);
          }
        }
      }
    }
    client.stop();
    Serial.println("Client disconnected");
  }
}
void sendCommandToSlave(String slaveIP, String rackList) {
  WiFiClient client;
  if (client.connect(slaveIP.c_str(), slave3Port)) {
    // 랙 리스트를 ','로 분할하여 각각에 "I,S"를 추가하여 전송
    int start = 0;
    int end = rackList.indexOf(',');
    while (end != -1) {
      String rack = rackList.substring(start, end);
      rack.trim();
      String command = rack + ",I,S";
      client.println(command);
      Serial.println("Sent command to slave: " + command);
      start = end + 1;
      end = rackList.indexOf(',', start);
    }
    // 마지막 랙 처리
    String rack = rackList.substring(start);
    rack.trim();
    String command = rack + ",I,S";
    client.println(command);
    Serial.println("Sent command to slave: " + command);

    delay(1000); // 모든 명령이 전송될 때까지 기다림
    client.stop();
  } else {
    Serial.println("Connection to slave failed: " + slaveIP);
  }
}

void checkInspectionComplete() {
  unsigned long currentMillis = millis();
  if (currentMillis - previousMillis >= interval) {
    previousMillis = currentMillis;

    // 슬레이브로부터 검사 완료 데이터를 요청
    requestInspectionComplete(SLAVE1_ADDR);
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
    Serial.println("Inspection completed for product:" + productCode);
    // 필요한 추가 작업 수행
    notifyNetworkManager("Inspection",productCode);
  }
}

void notifyNetworkManager(const String& task,const String& productCode) {
  WiFiClient client;
  Serial.println("Attempting to connect to network manager...");
  if (client.connect(MFCNetworkManagerIP.c_str(), networkManagerPort)) {
    String message = "result-"+task +":" + productCode;
    Serial.println(productCode);
    client.print(message);
    client.stop();
    Serial.println("Sent task completion to network_manager: " + message);
  } else {
    Serial.println("Connection to network_manager failed");
  }
}