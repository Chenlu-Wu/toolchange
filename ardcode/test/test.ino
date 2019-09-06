#include <Servo.h>
//Servo servo1;
Servo servo2;

int angle = 0;
int inpython = 0;
int val = 0;
int i = 0;
int a = 1;
void setup() {
  // put your setup code here, to run once:
//servo1.attach(7); //R-arm 1st
servo2.attach(8); //R-arm 2nd 
  Serial.begin(9600);
//servo1.write(120);
servo2.write(60);

}

void loop() {
  // put your main code here, to run repeatedly:


  if (a == 1) {
    if (Serial.available() > 0)
    {
      angle = Serial.parseInt();

    }
    if (angle != 0) {
      servo2.write(angle);
      Serial.println(angle); //for debugging
    }
    // a=0;
  }

}
