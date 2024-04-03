#include <TinkerKit.h>
#include <Servo.h>

//constants
Servo motorFL;
Servo motorFR;
Servo motorBL;
Servo motorBR;
Servo mount;
float inches;
float duration;
const int servoPin = 9;
const int pingPin = 7;

//Setup
void setup () {
  Serial.begin(9600);
  motorFL.attach(O0);
  motorFR.attach(O1);
  motorBL.attach(O2);
  motorBR.attach(O3);
  mount.attach(servoPin);
}

//Loop
void loop() {
  //detecting objects
  pinMode(pingPin, OUTPUT);
  digitalWrite(pingPin, LOW); //ensure pin is low
  delayMicroseconds(2);
  digitalWrite(pingPin, HIGH); //start ranging
  delayMicroseconds(5); //for 5 microseconds
  digitalWrite(pingPin, LOW); //end ranging
  pinMode(pingPin, INPUT);
  duration = pulseIn(pingPin, HIGH); //read echo pulse
  inches = duration / 74 / 2;

  //if encounters objects
  if (inches < 2) {
    motorFL.write(90);
    motorFR.write(90);
    motorBL.write(90);
    motorBR.write(90);
    delay(200);

    motorFL.write(180);
    motorFR.write(180);
    motorBL.write(0);
    motorBR.write(0);
    delay(2000);

    motorFL.write(180);
    motorFR.write(180);
    motorBL.write(0);
    motorBR.write(0);
    delay(1000);

    motorFL.write(0);
    motorFR.write(0);
    motorBL.write(180);
    motorBR.write(180);
    delay(1000);
    return;
  }
  else if (inches >= 2) {
    motorFL.write(180);
    motorFR.write(180);
    motorBL.write(180);
    motorBR.write(180);
  }
}
