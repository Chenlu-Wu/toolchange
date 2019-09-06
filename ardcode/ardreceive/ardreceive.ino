String cod="";
char line[500]="";
void setup(){
  
  Serial.begin(9600);
  while(Serial.read()>=0){} //clear serialbuffer
  
}

void loop(){
  

while (Serial.available()>0){
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
  
}

else if (cod[0]=='2'){

  Serial.println("Close fridge");
  
}

cod="";
}

}
