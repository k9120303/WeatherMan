#include <SoftwareSerial.h>
/*
序列埠要選沒有行結尾
AT：測試，回應「OK」
AT+VERSION：回應靭體的版本。
AT+NAMExyz：將裝置名稱改為「xyz」。
*/
SoftwareSerial BTSerial(10, 11); // RX | TX
void setup(){
Serial.begin(9600);
Serial.println("Enter AT commands:");
BTSerial.begin(9600);
}
void loop(){
if (BTSerial.available())
Serial.write(BTSerial.read()); 
if (Serial.available())
BTSerial.write(Serial.read());
}
