#include <LiquidCrystal.h>
#include <SoftwareSerial.h>


char c[20];
int s[4], sensorValue[4], sensorMax[4] = { 0 }, sensorMin[4] = { 1023 }, sensorAverage[3] = { 500,400,300};  //we can save sensorAverage according to the system or we calibrate sensor values.
void setup() {
  Serial.begin(9600);
  pinMode(A2, INPUT);
  pinMode(A1, INPUT);
  pinMode(A0, INPUT); 
    Serial.begin(9600);
  sensorCalibrate();
}
void wCase() {
  if (s[0] == 0 && s[1] == 0 && s[2] == 0) {
    strcpy(c, "HELPi-");
  } else if (s[0] == 0 && s[1] == 0 && s[2] == 1) {
    strcpy(c, "HAPPY");
  } else if (s[0] == 0 && s[1] == 1 && s[2] == 0) {
    strcpy(c, "NICE");
  } else if (s[0] == 0 && s[1] == 1 && s[2] == 1) {
    strcpy(c, "VICTORY");
  } else if (s[0] == 1 && s[1] == 0 && s[2] == 0) {
    strcpy(c, "We are rathinamites");
  } else if (s[0] == 1 && s[1] == 0 && s[2] == 1) {
    strcpy(c, "   ");
  } else if (s[0] == 1 && s[1] == 1 && s[2] == 0) {
    strcpy(c, "WORSHIP");
  } else /*if (s[0] == 1 && s[1] == 1 && s[2] == 1)*/ {
    strcpy(c, "DANGER");
  } 
 Serial.println(c);
 delay(1000);
}

void loop() {
  aRead();
  bAssign();
  wCase();
}
void aRead() {
  sensorValue[0] = analogRead(A0);
  sensorValue[1] = digitalRead(A1);
  sensorValue[2] = digitalRead(A2);
 
}
void bAssign() {
  if (sensorValue[0] > sensorAverage[0]) {
    s[0] = 0;

  } else {
    s[0] = 1;
  }
  if (sensorValue[1] > sensorAverage[1]) {
    s[1] = 0;

  } else {
    s[1] = 1;
  }
  if (sensorValue[2] > sensorAverage[2]) {
    s[2] = 0;

  } else {
    s[2] = 1;
  }
  }
void sensorCalibrate() {
  Serial.println("Calibrating..");
  for (int i = 0; i < 1000; i++) {
    aRead();
    if (sensorValue[0] > sensorMax[0])
    sensorMax[0] = sensorValue[0];
    if (sensorValue[0] < sensorMin[0])
    sensorMin[0] = sensorValue[0];

    if (sensorValue[1] > sensorMax[1])
      sensorMax[1] = sensorValue[1];
    if (sensorValue[1] < sensorMin[1])
      sensorMin[1] = sensorValue[1];

    if (sensorValue[2] > sensorMax[2])
      sensorMax[2] = sensorValue[2];
    if (sensorValue[2] < sensorMin[2])
      sensorMin[2] = sensorValue[2];

    delay(5);
  }
  sensorAverage[0] = (sensorMax[0] + sensorMin[0]) / 2;
  sensorAverage[1] = (sensorMax[1] + sensorMin[1]) / 2;
  sensorAverage[2] = (sensorMax[2] + sensorMin[2]) / 2; 
  Serial.println(sensorAverage[0]);
  Serial.println(sensorAverage[1]);
  Serial.println(sensorAverage[2]);
}
