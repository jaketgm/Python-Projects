int triggerPin = 2;
int hPin = A0;
int vPin = A1;
float H = 0;
float V = 0;

void setup() {
  pinMode(13, OUTPUT);
  pinMode(triggerPin, OUTPUT);
  Serial.begin(9600);
}

int Random() {
  digitalWrite(triggerPin, HIGH);
  delay(3);
  digitalWrite(triggerPin, LOW);
  //Photoresistor reading
  H = analogRead(hPin);
  V = analogRead(vPin);
  //Determine random bit
  if (H > V) { //More photons in the H mode, return 0
    return 0;
  } if (H < V) {
    return 1;
  } else {
    Random();
  }
  
}

void loop() {
  Serial.print(Random());
}
