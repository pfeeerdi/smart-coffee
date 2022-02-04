#ifndef ARDUINO_CREDENTIALS_H
#define ARDUINO_CREDENTIALS_H

/* WiFi Credentials to connect Internet */
#define STA_SSID "Wlan 2"
#define STA_PASS "Geodreieck54!"

/* Provide MQTT broker credentials as denoted in maqiatto.com. */
#define MQTT_BROKER       "maqiatto.com"
#define MQTT_BROKER_PORT  1883
#define MQTT_USERNAME     "ferdi9@hotmail.de"
#define MQTT_KEY          "vEC7JNU2dERes8C"


/* Provide topic as it is denoted in your topic list. 
 * For example mine is : cadominna@gmail.com/topic1
 * To add topics, see https://www.maqiatto.com/configure
 */
#define COFFEE_HIST_TOPIC    "ferdi9@hotmail.de/coffeeshistory"
#define COFFEE_MAKE_TOPIC    "ferdi9@hotmail.de/makecoffee"

#endif /* ARDUINO_CREDENTIALS_H */
