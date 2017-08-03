#include <SoftwareSerial.h> //libaray of I2C
#include <SimpleDHT.h>

SoftwareSerial BT(10,11); //define serial BT  RX, TX

// for DHT11, 
//      VCC: 5V or 3V
//      GND: GND
//      DATA: 2
// for PIR, 
//      VCC: 5V 
//      GND: GND
//      DATA: 3

int pinDHT11 = 2;
int pinPIR=3;
int pinPho=A2;
SimpleDHT11 dht11;
int time = millis(); //millisceond
void setup()
{
  Serial.begin(9600);
  BT.begin(9600);
  pinMode(13, OUTPUT);
  pinMode(pinPIR, INPUT);
}

void loop()
{
  int valPIR=digitalRead(pinPIR);
  int valPho=analogRead(pinPho);
  valPho=valPho/10;
  byte temperature = 0;
  byte humidity = 0;
  delay(1000);
  if (dht11.read(pinDHT11, &temperature, &humidity, NULL)) {
    Serial.println("Read DHT11 failed.");
    return;
  }
  Serial.print("DHT11 OK: ");
  Serial.print(temperature); Serial.print(" *C, "); Serial.print(humidity); Serial.println(" %, "); 
  if (valPIR==HIGH) {
    Serial.println("PIR capture something : ");
    //PIR 有偵測到時 : LED 閃一下
    digitalWrite(13,HIGH);
    }
  else {  //PIR 沒有偵測到 : LED 暗
    digitalWrite(13,LOW);
    Serial.println("PIR capture nothing : ");
    }
   Serial.print("Pho value : ");Serial.println(valPho);
    Serial.println("/////////////////////////////////");
    Serial.println(" ");
   //delay(500);
   
  int testdata[5]={0,0,0,0,0};
  int now_time = millis();
  if((now_time - time) >= 100)     //actives every 100 milliseconds
  {
    testdata[0]=valPho;
    testdata[1]=valPIR;
    testdata[2]=temperature;
    testdata[3]=humidity;
        BT.write(200); //send packet to phone
        //BT.write(testdata[0]); //send packet to phone
        //BT.write(testdata[1]); //send packet to phone
        BT.write(testdata[2]); //send packet to phone
        BT.write(testdata[3]); //send packet to phone
    
    //Serial.print("PP_status: ");Serial.println(pp_statue);
    time = now_time;
  }
  
}

