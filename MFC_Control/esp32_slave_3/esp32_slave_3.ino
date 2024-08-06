#include <WiFi.h>
#include <WiFiClient.h>
#include <WiFiServer.h>
#include <Adafruit_NeoPixel.h>

const char* ssid = "Tmwlakfk_>u<";
const char* password = "96989898";

WiFiServer server(80); // 포트 80에서 서버를 시작

// NeoPixel 핀 배열 (각 핀에 두 개의 NeoPixel)
int ledPins[] = {2, 4, 22, 23, 18, 19, 21, 13, 12, 14, 27, 26, 25, 33};
#define NUMPIXELS 2 // 각 핀에 연결된 NeoPixel 수

// 각 NeoPixel 객체를 관리하기 위한 배열
Adafruit_NeoPixel* pixels[sizeof(ledPins) / sizeof(ledPins[0])];
bool initialized[sizeof(ledPins) / sizeof(ledPins[0])] = {false};

void setup() {
  Serial.begin(9600);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }
  Serial.println("Connected to WiFi");
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP()); // 슬레이브 IP 주소 출력

  server.begin(); // 서버 시작
}

void loop() {
  // 클라이언트 요청 처리
  WiFiClient client = server.available();
  if (client) {
    Serial.println("Client connected");
    while (client.connected()) {
      if (client.available()) {
        String request = client.readStringUntil('\n');
        request.trim(); // 입력 문자열에서 공백 제거
        Serial.println("Received: " + request);

        processCommand(request); // 명령 처리
        client.flush();
      }
    }
    client.stop();
    Serial.println("Client disconnected");
  }
}

// 명령 처리 함수
void processCommand(String input) {
  if (input.length() < 7) {
    Serial.println("Invalid input format.");
    return;
  }

  // 공백이 제거된 입력 문자열에서 구분자를 기준으로 나누기
  int firstComma = input.indexOf(',');
  int secondComma = input.indexOf(',', firstComma + 1);

  if (firstComma == -1 || secondComma == -1) {
    Serial.println("Invalid input format.");
    return;
  }

  String rack = input.substring(0, firstComma);
  rack.trim();
  char side = input.charAt(firstComma + 1);
  char action = input.charAt(secondComma + 1);

  Serial.print("Received command: rack="); Serial.print(rack);
  Serial.print(", side="); Serial.print(side);
  Serial.print(", action="); Serial.println(action);

  int ledIndex = getLedIndex(rack);
  if (ledIndex != -1) {
    if (!initialized[ledIndex]) {
      initializePin(ledIndex);
    }

    if (side == 'I' && action == 'S') {
      // 오른쪽 빨간 LED ON
      pixels[ledIndex]->setPixelColor(1, pixels[ledIndex]->Color(255, 0, 0));
      Serial.print("Set right LED to RED on pin "); Serial.println(ledPins[ledIndex]);
    } else if (side == 'O' && action == 'S') {
      // 왼쪽 파란 LED ON
      pixels[ledIndex]->setPixelColor(0, pixels[ledIndex]->Color(0, 0, 255));
      Serial.print("Set left LED to BLUE on pin "); Serial.println(ledPins[ledIndex]);
    } else if (side == 'I' && action == 'F') {
      // 오른쪽 빨간 LED OFF
      pixels[ledIndex]->setPixelColor(1, pixels[ledIndex]->Color(0, 0, 0));
      Serial.print("Turned off right LED on pin "); Serial.println(ledPins[ledIndex]);
    } else if (side == 'O' && action == 'F') {
      // 왼쪽 파란 LED OFF
      pixels[ledIndex]->setPixelColor(0, pixels[ledIndex]->Color(0, 0, 0));
      Serial.print("Turned off left LED on pin "); Serial.println(ledPins[ledIndex]);
    }

    pixels[ledIndex]->show(); // 업데이트 적용
    Serial.print("Processed command: "); Serial.println(input);
  } else {
    Serial.println("Invalid rack identifier.");
  }
}

// 요청에 따른 LED 인덱스 반환 함수
int getLedIndex(String rack) {
  rack.trim(); // 비교 전에 공백 제거
  Serial.print("Comparing rack: "); Serial.println(rack); // 디버그용 출력

  if (rack == "R_A1") return 0;
  if (rack == "R_A2") return -1; // 제외된 핀
  if (rack == "R_A3") return 1;
  if (rack == "R_B1") return -1; // 제외된 핀
  if (rack == "R_B2") return 2;
  if (rack == "R_B3") return 3;
  if (rack == "R_C1") return 4;
  if (rack == "R_C2") return 5;;
  if (rack == "R_C3") return 6;
  if (rack == "R_D1") return 7;
  if (rack == "R_D2") return 8;
  if (rack == "R_D3") return 9;
  if (rack == "R_E1") return 10;
  if (rack == "R_E2") return -1; // 제외된 핀
  if (rack == "R_E3") return 11;
  if (rack == "R_F1") return 12;
  if (rack == "R_F2") return 13;
  if (rack == "R_F3") return -1; // 제외된 핀
  return -1; // 잘못된 요청
}

// 핀 초기화 함수
void initializePin(int index) {
  pixels[index] = new Adafruit_NeoPixel(NUMPIXELS, ledPins[index], NEO_GRB + NEO_KHZ800);
  pixels[index]->begin();
  pixels[index]->show(); // 초기화 상태로 LED를 꺼둠
  Serial.print("Initialized pin "); Serial.println(ledPins[index]);
  initialized[index] = true;
}
