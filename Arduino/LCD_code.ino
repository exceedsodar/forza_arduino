#include <LiquidCrystal.h> 
int Contrast=125;
int val = 0;
volatile byte state = LOW;
 LiquidCrystal lcd(12, 11, 8, 7, 6, 5);  

 void setup()
 {
  pinMode(2, INPUT_PULLUP); 
  pinMode(13, OUTPUT); 
  digitalWrite(13,state);
    analogWrite(9,Contrast);
     lcd.begin(16, 2);

     attachInterrupt(digitalPinToInterrupt(2), blink, RISING );
  } 
  
     void loop()
 { 
     lcd.setCursor(0, 0);
     lcd.print(millis() / 1000);
    val = digitalRead(2);   // read the input pin
    state = val;
    digitalWrite(13,state);
  // set the cursor to column 0, line 1
  // (note: line 1 is the second row, since counting begins with 0):
  lcd.setCursor(0, 1);
  // print the number of seconds since reset:
  lcd.print(Contrast);
 }

 void blink()
  {
  delay(500);
   Contrast++;
   analogWrite(9,Contrast);
   
  }
