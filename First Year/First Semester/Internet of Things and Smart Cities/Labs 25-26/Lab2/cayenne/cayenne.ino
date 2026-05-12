// Before running edit properly line 42 and 43

#include <MKRWAN.h>
#include <CayenneLPP.h>

LoRaModem modem;

//edit with your own appEui and appKey
String appEui = "DDADADBA12EAAADA";
String appKey = "97E8F1934BC7E2D6DFBEAF03C9E39C81";

CayenneLPP lpp(51);

void setup() {
  int connected;
  Serial.begin(115200);
  while (!Serial);

  if (!modem.begin(EU868)) {
    Serial.println("Failed to start module");
    while (1) {}
  };
  
  Serial.print("Your device EUI is: ");
  Serial.println(modem.deviceEUI());

  connected = modem.joinOTAA(appEui, appKey);

  if (!connected) {
    Serial.println("Something went wrong; are you indoor? Move near a window and retry");
    while (1) {}
  }
  Serial.println("Succesfully Joined to the network!");
  randomSeed(analogRead(0));
}

void wait(int seconds) {
  int j=0;
  while(j<seconds*2){
    delay(500);
    Serial.print("=");
    j++;
  }
  Serial.print("\n");
}

void printVariables(){
  lpp.reset();
  float humidity = random(800, 1001) / 20.0;
  float pressure = random(1013, 1033) / 100.0;
  float pH = random(699, 702) / 100.0;

  float temperature1 = random(1500, 3501) / 100.0;
  float temperature2 = random(1500, 3501) / 100.0;
  float temperature3 = random(1500, 3501) / 100.0;

  //lpp.addRelativeHumidity(3, humidity);
  //lpp.addTemperature(4, temperature);
  //lpp.addBarometricPressure(7, pressure);
  //lpp.addAnalogInput(8, pH);

  lpp.addAnalogInput(1, temperature1);
  lpp.addAnalogInput(2, temperature2);
  lpp.addAnalogInput(3, temperature3);
}

void loop() {
  Serial.println("Waiting 1 minute to send next message");
  wait(60);
  while (modem.available()) {
    Serial.write(modem.read());
  }
  modem.poll();

  int err;
  modem.setPort(3);
  modem.beginPacket();
  printVariables();
  modem.write(lpp.getBuffer(), lpp.getSize());
  err = modem.endPacket(true);
  if (err > 0) {
    Serial.println("Message sent correctly!");
  } else {
    Serial.println("Error sending message :(");
  }
}