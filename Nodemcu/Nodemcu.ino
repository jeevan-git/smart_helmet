#include <ESP8266WiFi.h>
#include <PubSubClient.h>

const char* ssid = "Sapan WIFI";
const char* password = "sapanbogati7";

// Change the variable to your Raspberry Pi IP address, so it connects to your MQTT broker
const char* mqtt_server = "192.168.0.103";

const int led_pin = D4;
const int relay_pin_ = D4;

// Initializes the espClient
WiFiClient espClient;
PubSubClient client(espClient);

// DHT Sensor

void setup_wifi() {
  delay(10);
  // We start by connecting to a WiFi network
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.print("WiFi connected - ESP IP address: ");
  Serial.println(WiFi.localIP());
}


void callback(String topic, byte* message, unsigned int length) {
  String messageTemp;

  for (int i = 0; i < length; i++) {
    Serial.println((char)message[i]);
    messageTemp += (char)message[i];
  }
  if (messageTemp == "1")
  {
    digitalWrite(led_pin, LOW);
    digitalWrite(relay_pin_, HIGH);
  }
  else if (messageTemp == "0") {
    digitalWrite(led_pin, HIGH);
    digitalWrite(relay_pin_, LOW);
  }
}

void reconnect() {
  // Loop until we're reconnected
  while (!client.connected()) {
    Serial.print("Attempting MQTT connection...");

    if (client.connect("ESP8266Client")) {
      Serial.println("connected");
      client.subscribe("relay_topic");
    }
    else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      delay(15000);
    }
  }
}

void setup() {

  Serial.begin(115200);
  setup_wifi();
  client.setServer(mqtt_server, 1883);
  client.setCallback(callback);
  pinMode(led_pin, OUTPUT);
  pinMode(relay_pin_, OUTPUT);
  digitalWrite(led_pin, HIGH);
  digitalWrite(relay_pin_, LOW);
}

void loop() {
  if (!client.connected()) {
    reconnect();
  }
  if (!client.loop())
    client.connect("ESP8266Client");
  if (digitalRead(led_pin) == true) {
    client.publish("relay_status", "0");
  }
  else if (digitalRead(led_pin) == false) {
    client.publish("relay_status", "1");
  }
  //  client.subscribe("/esp8266");
}
