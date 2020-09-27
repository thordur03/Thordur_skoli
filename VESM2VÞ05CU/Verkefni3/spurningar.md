# 3.1
1. pi er mikið öflugri og er með stýrikerfi en arduino tekur bara inn signal frá pinnum og sendir signal frá þeim
    og þarf að flasha kóðann yfir með aðrari tölvu
2. ef maður er með mikið af tengingum eða langtfrá öðrum t.d. margir hitamælir og hitastjórn tengd with mörg arduino í kringum skólann og svo eitt pi í miðjunni sem tekur inn allar upplýsingarnar og reinir að halda meðal hitanum í 28
# 3.2
## pi kóði

import serial
import RPi.GPIO as GPIO
import time

ser=serial.Serial("/dev/ttyACM0",9600)  #change ACM number as found from ls /dev/tty/ACM*
ser.baudrate=9600
def blink(pin):


GPIO.output(pin,GPIO.HIGH)  
time.sleep(1)  
GPIO.output(pin,GPIO.LOW)  
time.sleep(1)  
return

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
while True:

  read_ser=ser.readline()
  msg = read_ser.decode('utf-8') # To convert byte strings to Unicode, líka hægt að nota bytes.decode(read_ser)
  print(msg) 
  if(msg.strip()=="Hello From Arduino!"):
    blink(11)
## arduino kóði

String data="Hello From Arduino!";

void setup() {
// put your setup code here, to run once:
Serial.begin(9600);

}

void loop() {
// put your main code here, to run repeatedly:
Serial.println(data);//data that is being Sent
delay(200);
}
https://www.youtube.com/watch?v=NWM92zt1xms

# 3.3

## pi kóði
import serial
import time
ser = serial.Serial('/dev/ttyACM1', 9600)
while True:
    ser.write(str.encode('6'))
    time.sleep(1)
    ser.write(str.encode('5'))
    time.sleep(1)
    ser.write(str.encode('3'))
    time.sleep(1)

## Arduino Kóði

char receivedChar;
boolean newData = false;

void setup() {

  Serial.begin(9600);

  pinMode(3, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
  
}

void loop() {

  recvInfo();
  lightLED();
  
}

void recvInfo() {

  if (Serial.available() > 0) {

    receivedChar = Serial.read();
    newData = true;
    
  }

https://www.youtube.com/watch?v=lV6VNczPEUs

