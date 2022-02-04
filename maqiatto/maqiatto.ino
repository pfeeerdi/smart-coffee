#include <ESP8266WiFi.h>
#include <Arduino.h>

#include "MQTTConnector.h"
#include "Credentials.h"

#define WIFI_TIMEOUT 5000
#define LOOP_TIMEOUT 100

#define EspressoPin 14
#define DoubleEspressoPin 13
#define buttonPin 4


void WiFiBegin(const char* ssid, const char* pass)
{
  WiFi.begin(ssid, pass);
  Serial.printf("Waiting for AP connection ...\n");
  while(WiFi.status() != WL_CONNECTED)
  {
    delay(WIFI_TIMEOUT);
    Serial.printf(".");
  }
  IPAddress ip = WiFi.localIP();
  Serial.printf("\nConnected to AP. IP : %d.%d.%d.%d\n", 
    ip[0],ip[1],ip[2],ip[3]);
}

void setup() 
{
  Serial.begin(9600);
  Serial.setDebugOutput(true);
  WiFiBegin(STA_SSID, STA_PASS);
  MQTTBegin();
  TimeBegin();
  pinMode(EspressoPin, OUTPUT);
  pinMode(DoubleEspressoPin, OUTPUT);
  pinMode(buttonPin, INPUT);
  
}

void loop() 
{
  MQTTLoop();
  CoffeeLoop();
  delay(LOOP_TIMEOUT);
}
