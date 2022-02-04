#include <ESP8266WiFi.h>
#include <PubSubClient.h>

#include "MQTTConnector.h"
#include "Credentials.h"

WiFiClient wifiClient;
PubSubClient mqttClient(wifiClient);


boolean mqttInitCompleted = false;
String clientId = "IoTPractice-" + String(ESP.getChipId());


//Coffee and Time Setup
#include <NTPClient.h>
#include <WiFiUdp.h>


WiFiUDP ntpUDP;
NTPClient timeClient(ntpUDP, "pool.ntp.org");

void TimeBegin()
{
  timeClient.begin();
  timeClient.setTimeOffset(3600);
}

String getdatetime()
{
  timeClient.update();
    String formattedTime = timeClient.getFormattedTime();
    //Serial.print("Formatted Time: ");
    //Serial.println(formattedTime);
    
    unsigned long epochTime = timeClient.getEpochTime();
    time_t rawtime = epochTime;
    struct tm *ptm = gmtime(&rawtime);
    int monthDay = ptm->tm_mday;
    int currentMonth = ptm->tm_mon+1;
    int currentYear = ptm->tm_year+1900;
    
    
    String currentDate = String(currentYear) + "-" + String(currentMonth) + "-" + String(monthDay);
    //Serial.print("Current date: ");
    //Serial.println(currentDate);
    return (currentDate + ", " + formattedTime);
}

void makeCoffee(int CoffeePin)
{
  digitalWrite(CoffeePin, HIGH);
  delay(2000);
  digitalWrite(CoffeePin, LOW);
}

void publishCoffee(String CoffeeType)
{
    String answer = (getdatetime() + ", " + CoffeeType);
    char* char_answer = &answer[0];
    if(MQTTPublish(COFFEE_HIST_TOPIC, char_answer))
    {
      Serial.printf("MQTTPublish was succeeded.\n");
    }
}

//function to brew coffee by Type (espresso or double_espresso)
boolean MQTTMakeCoffee(String CoffeeType)
{
  boolean retval = true;
  if (CoffeeType == "espresso")
  {
    Serial.printf("Making a espresso! (D5)\n");
    makeCoffee(14);
    publishCoffee(CoffeeType);
    delay(15000);
  }
  else if (CoffeeType == "double_espresso")
  {
    Serial.printf("Making a double espresso! (D7)\n");
    makeCoffee(13);
    publishCoffee(CoffeeType);
    delay(15000);
  }
  else //if none of the above is true
  {
    retval = false;
    Serial.printf("Error receiving CoffeeType \n", CoffeeType);
  }
  return retval;
}






/* Incoming data callback. */
void dataCallback(char* topic, byte* payload, unsigned int length)
{
  char payloadStr[length + 1];
  memset(payloadStr, 0, length + 1);
  strncpy(payloadStr, (char*)payload, length);
  Serial.printf("Data    : dataCallback. Topic : [%s]\n", topic);
  Serial.printf("Data    : dataCallback. Payload : %s\n", payloadStr);
  MQTTMakeCoffee(payloadStr);
}


void performConnect()
{
  uint16_t connectionDelay = 5000;
  while (!mqttClient.connected())
  {
    Serial.printf("Trace   : Attempting MQTT connection...\n");
    if (mqttClient.connect(clientId.c_str(), MQTT_USERNAME, MQTT_KEY))
    {
      Serial.printf("Trace   : Connected to Broker.\n");

      /* Subscription to your topic after connection was succeeded.*/
      MQTTSubscribe(COFFEE_MAKE_TOPIC);
    }
    else
    {
      Serial.printf("Error!  : MQTT Connect failed, rc = %d\n", mqttClient.state());
      Serial.printf("Trace   : Trying again in %d msec.\n", connectionDelay);
      delay(connectionDelay);
    }
  }
}

boolean MQTTPublish(const char* topic, char* payload)
{
  boolean retval = false;
  if (mqttClient.connected())
  {
    retval = mqttClient.publish(topic, payload);
  }
  return retval;
}

boolean MQTTSubscribe(const char* topicToSubscribe)
{
  boolean retval = false;
  if (mqttClient.connected())
  {
    retval = mqttClient.subscribe(topicToSubscribe);
  }
  return retval;
}

boolean MQTTIsConnected()
{
  return mqttClient.connected();
}

void MQTTBegin()
{
  mqttClient.setServer(MQTT_BROKER, MQTT_BROKER_PORT);
  mqttClient.setCallback(dataCallback);
  mqttInitCompleted = true;
}

void MQTTLoop()
{
  if(mqttInitCompleted)
  {
    if (!MQTTIsConnected())
    {
      performConnect();
    }
    mqttClient.loop();
  }
}

void CoffeeLoop(){
  //if under 415 and above 390 --> coffe is made
  int number = analogRead(A0);
  if ((390 < number) && (number < 410)){
     Serial.println("Coffee is made");
     //Serial.println(number);
     publishCoffee("espresso");
     delay(15000);
     Serial.println("Done with brewing coffee");
  }
}
