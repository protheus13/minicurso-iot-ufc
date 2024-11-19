/*
    Go to thingspeak.com and create an account if you don't have one already.
    After logging in, click on the "New Channel" button to create a new channel for your data. This is where your data will be stored and displayed.
    Fill in the Name, Description, and other fields for your channel as desired, then click the "Save Channel" button.
    Take note of the "Write API Key" located in the "API keys" tab, this is the key you will use to send data to your channel.
    Replace the channelID from tab "Channel Settings" and privateKey with "Read API Keys" from "API Keys" tab.
    Replace the host variable with the thingspeak server hostname "api.thingspeak.com"
    Upload the sketch to your ESP32 board and make sure that the board is connected to the internet. The ESP32 should now send data to your Thingspeak channel at the intervals specified by the loop function.
    Go to the channel view page on thingspeak and check the "Field1" for the new incoming data.
    You can use the data visualization and analysis tools provided by Thingspeak to display and process your data in various ways.
    Please note, that Thingspeak accepts only integer values.

    You can later check the values at https://thingspeak.com/channels/2005329
    Please note that this public channel can be accessed by anyone and it is possible that more people will write their values.
 */

// #include <ESP8266WiFi.h>
#include <WiFi.h>

const char* ssid     = "LOGIN"; // Change this to your WiFi SSID
const char* password = "senha"; // Change this to your WiFi password

const char* host = "api.thingspeak.com"; // This should not be changed
const int httpPort = 80; // This should not be changed
const String channelID   = ""; // Change this to your channel ID
const String writeApiKey = ""; // Change this to your Write API key
const String readApiKey = ""; // Change this to your Read API key

const int PINO_TRIG = 5; // Pino D4 conectado ao TRIG do HC-SR04
const int PINO_ECHO = 4; // Pino D2 conectado ao ECHO do HC-SR04
#define LED_BUILTIN 2
int numberOfResults = 3; // Number of results to be read
int fieldNumber = 1; // Field number which will be read out

void setup()
{
    Serial.begin(115200);
    while(!Serial){delay(100);}
    pinMode(PINO_ECHO, INPUT);
    pinMode(PINO_TRIG, OUTPUT);

    // We start by connecting to a WiFi network
    pinMode(LED_BUILTIN, OUTPUT);
    Serial.println();
    Serial.println("******************************************************");
    Serial.print("Connecting to ");
    Serial.println(ssid);

    WiFi.begin(ssid, password);

    while (WiFi.status() != WL_CONNECTED) {
        delay(500);
        Serial.print(".");
    }

    Serial.println("");
    Serial.println("WiFi connected");
    Serial.println("IP address: ");
    digitalWrite(LED_BUILTIN, HIGH);
    Serial.println(WiFi.localIP());
}

void readResponse(WiFiClient *client){
  unsigned long timeout = millis();
  while(client->available() == 0){
    if(millis() - timeout > 5000){
      Serial.println(">>> Client Timeout !");
      client->stop();
      return;
    }
  }

  // Read all the lines of the reply from server and print them to Serial
  while(client->available()) {
    String line = client->readStringUntil('\r');
    Serial.print(line);
  }

  Serial.printf("\nClosing connection\n\n");
}

void loop(){
  WiFiClient client;
  digitalWrite(PINO_TRIG, LOW);
  delayMicroseconds(2);
  digitalWrite(PINO_TRIG, HIGH);
  delayMicroseconds(10);
  digitalWrite(PINO_TRIG, LOW);
  
  long duracao = pulseIn(PINO_ECHO, HIGH); // Mede o tempo de resposta do ECHO  
  float distancia = (duracao * 0.0343) / 2;// Calcula a distância usando a velocidade do som (aproximadamente 343 m/s)
  Serial.print("Nível da água (cm): ");
  float nivel = distancia;
  Serial.print(nivel);
  Serial.println(" cm");

  delay(200);
  if (isnan(distancia))
    {
      Serial.println("Failed to read from sensor!");
      return;
    }
  if (client.connect(host,80)) // "184.106.153.149" or api.thingspeak.com
    {
      String postStr = writeApiKey;
      postStr +="&field1="; // atenção, esse é o campo 1 que você escolheu no canal do ThingSpeak
      postStr += String(nivel);
      postStr += "\r\n\r\n";
      String footer = String(" HTTP/1.1\r\n") + "Host: " + String(host) + "\r\n" + "Connection: close\r\n\r\n";

    // WRITE --------------------------------------------------------------------------------------------
  if (!client.connect(host, httpPort)) {
      return;
    }

      client.print("POST /update?api_key=" + writeApiKey + "&field1=" + nivel + footer);
      readResponse(&client);
      digitalWrite(LED_BUILTIN, HIGH);
      client.print(postStr.length());
      client.print("\n\n");
      client.print(postStr);
      Serial.print("Nível de água (cm): ");
      Serial.print(nivel);
      Serial.print(" cm");
      Serial.println("");
      delay(1000);
    }
  client.stop();
  digitalWrite(LED_BUILTIN, LOW);
  delay(19000);
}