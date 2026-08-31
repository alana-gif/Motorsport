//DONT TOUCH
//CURRENTY WORKS

const int potPin = A0;

const int ledPins[] = {8, 7, 6, 5, 4, 3, 2}; //in reverse //no longer
const int numLeds = 7;

void setup() {
  for (int i = 0; i < numLeds; i++) {
    pinMode(ledPins[i], OUTPUT);
  }
  Serial.begin(9600);
}

void loop() {
  int potValue = analogRead(potPin);  // 0–1023

  // Map pot value to number of LEDs (0–5)
  int ledLevel = map(potValue, 0, 1023, 0, numLeds);

  // Turn LEDs on/off
  for (int i = 0; i < numLeds; i++) {
    if (i < ledLevel) { //mabye change here for pot
      digitalWrite(ledPins[i], HIGH);
    } else {
      digitalWrite(ledPins[i], LOW);
    }
  }

  Serial.println(potValue); // Optional: see values in Serial Monitor
  delay(500);
}