// Before running edit properly line 42 and 43

#include <MKRWAN.h>

LoRaModem modem;

String appEui;
String appKey;
String devAddr;
String nwkSKey;
String appSKey;

String messages [4]  = {"Welcome to IoT Lab", "This lab is amazing", "We will work with TTN" , "A few Arduino too <3"};
int i = 0;

void setup() {
  int connected;
  float a = 20.0f;
  // put your setup code here, to run once:
  Serial.begin(115200);
  while (!Serial);

  // change this to your regional band (eg. US915, AS923, ...)
  if (!modem.begin(EU868)) {
    Serial.println("Failed to start module");
    while (1) {}
  };
  
  
  Serial.print("Your device EUI is: ");
  Serial.println(modem.deviceEUI());

  //edit with your own appEui and appKey
  appEui = "2102030608247211";
  appKey = "38F37503EE2236A01DB430F00F3920A8";

  connected = modem.joinOTAA(appEui, appKey);
  

  if (!connected) {
    Serial.println("Something went wrong; are you indoor? Move near a window and retry");
    while (1) {}
  }
  Serial.println("Succesfully Joined to the network!");

}

void loop() {
Serial.println("Waiting 1 minute to send next message");
  int j=0;
  while(j<120){
  delay(500);
  Serial.print("=");
  j++;
  }
  Serial.print("\n");
  while (modem.available()) {
    Serial.write(modem.read());
  }
  modem.poll();
  

  int err;
  modem.setPort(3);
  modem.beginPacket();
  modem.print(messages[i%4]);
  modem.write(a);
  err = modem.endPacket(true);
  if (err > 0) {
    i = i+1;
    Serial.println("Message sent correctly!");
  } else {
    Serial.println("Error sending message :(");
  }

}