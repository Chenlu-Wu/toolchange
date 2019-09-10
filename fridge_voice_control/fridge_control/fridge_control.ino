#include <Servo.h>
Servo servo1;
Servo servo2;

int angle = 0;
int inpython = 0;
int val = 0;
int i = 0;
int a = 1; 

String cod="";

void setup(){
  
  servo1.attach(7); //flick
  servo2.attach(8); //swing open
  
  Serial.begin(9600);
  
  servo1.write(0);
  servo2.write(90);
 
  while(Serial.read()>=0){} //clear serialbuffer
  
}

void loop(){
  

while (Serial.available()>0){
  Serial.write(1);
  delay (100);
  int numdata=Serial.available();
  Serial.print("Serial.available=");
  Serial.println(numdata);
  
  cod+=char(Serial.read());
  Serial.print("cod is");
  Serial.println(cod);
  delay(50);

//while (Serial.read()>=0){} // clear serial buffer
  
}
if (cod.length()>0){
  
  Serial.println(cod);
  Serial.print("cod[0]");
  Serial.println(cod[0]);

if (cod[0]=='1'){
  
    Serial.println("Open fridge");
  
    for (i=0; i<=25; i++){
      servo1.write(i);
      servo2.write(85);
      Serial.print("Flick angle=");
      Serial.println(i); //for debugging
      delay(50);
    }
    for (i=85;i>=5;i--){
      servo1.write(25);
      servo2.write(i);
      delay(50);    
      }

      for (i=25; i>=0; i--){
      servo1.write(i);
      servo2.write(5);
      Serial.print("Swing angle=");
      Serial.println(i); 
      delay(20);
      }
  
}

else if (cod[0]=='2'){

     Serial.println("Close fridge");
  
     for (i=5;i<=90;i++){
      servo1.write(0);
      servo2.write(i);
      delay(50);    
      }
  
}

cod="";
}

}
