#ifndef ARDUINO_MQTTCONNECTOR_H
#define ARDUINO_MQTTCONNECTOR_H

#include <Arduino.h>

void    MQTTBegin();
void    TimeBegin();
void    MQTTLoop();
void    CoffeeLoop();
boolean MQTTPublish(const char* topic, char* payload);
boolean MQTTSubscribe(const char* topicToSubscribe);
boolean MQTTIsConnected();

#endif /* ARDUINO_MQTTCONNECTOR_H */
