void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(leftmotor1, OUTPUT);
  pinMode(leftmotor2, OUTPUT);
  pinMode(rightmotor1, OUTPUT);
  pinMode(rightmotor2, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  int A;
  A = Serial.read();
  if (A == 1) // go forward
  {
    digitalWrite(leftmotor1, HIGH);
    digitalWrite(leftmotor2, LOW);
    digitalWrite(rightmotor2, HIGH);
    digitalWrite(rightmotor2, LOW);
    delay(2000);
  }
  if (A == 2) // go backwards
  {
    digitalWrite(leftmotor1, LOW);
  }

}
