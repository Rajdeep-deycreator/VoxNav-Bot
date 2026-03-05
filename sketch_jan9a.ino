#include <Servo.h>

bool tymode=false;
const int lback=2;
const int lfront=3;
const int rfront=4;
const int rback=5;
const int echo=12;
const int trig=13;

Servo head;
Servo larm;
Servo rarm;
void front(){
  digitalWrite(lfront,HIGH);
  digitalWrite(rfront,HIGH);
  digitalWrite(lback,LOW);
  digitalWrite(rback,LOW);
  lofront();

}
void lofront(){
  head.write(90);
}
void loleft(){
  head.write(180);
  digitalWrite(lfront,LOW);
  digitalWrite(lback,HIGH);
  digitalWrite(rfront,HIGH);
  digitalWrite(rback,LOW);
  delay(4000);
  stop();
  delay(1000);
  lofront();
}
void loright(){
  head.write(0);
  digitalWrite(lfront,HIGH);
  digitalWrite(lback,LOW);
  digitalWrite(rfront,LOW);
  digitalWrite(rback,HIGH);
  delay(4000);
  stop();
  delay(1000);
  lofront();
}
void stop(){
  digitalWrite(lfront,LOW);
  digitalWrite(rfront,LOW);
  digitalWrite(lback,LOW);
  digitalWrite(rback,LOW);
}
void hi(){
  rarm.write(45);
  delay(1000);
  rarm.write(0);
  delay(1000);
  rarm.write(70);
  delay(1000);
  rarm.write(0);
}
long distance(){
  digitalWrite(trig,LOW);
  delayMicroseconds(2);
  digitalWrite(trig,HIGH);
  delayMicroseconds(10);
  digitalWrite(trig,LOW);

  long time=pulseIn(echo,HIGH,30000);
  if(time==0) return 999;
  else{
    long dist=(time*0.034)/2;
    return dist;
  }
}
void setup() {
  Serial.begin(9600);
  pinMode(lfront,OUTPUT);
  pinMode(lback,OUTPUT);
  pinMode(rfront,OUTPUT);
  pinMode(rback,OUTPUT);
  pinMode(echo,INPUT);
  pinMode(trig,OUTPUT);
  head.attach(9);
  head.write(90);
  larm.attach(8);
  larm.write(0);
  rarm.attach(10);
  rarm.write(0);
  
}
void loop() {
  if(Serial.available()){
    String r=Serial.readString();
    r.trim();
    Serial.print(r);
    if (r.indexOf("ty") !=-1){
      tymode=true;
      
    }
    if (r.indexOf("s") !=-1){
      stop();
      tymode=false;
    }
    if (r.indexOf("lf") !=-1){
      lofront();
    }
    if (r.indexOf("ll") !=-1){
      loleft();
    }
    if (r.indexOf("lr") !=-1){
      loright();
    }
    if(r.indexOf("hi") !=-1){
      hi();
    }
  }
  if(tymode){
        long di=distance();
        Serial.println(di);
        if(di <= 15){
          stop();
          delay(900);
          loright();
          delay(1500);
          head.write(90);
        }else{
          front();
        }
      }
  
}
