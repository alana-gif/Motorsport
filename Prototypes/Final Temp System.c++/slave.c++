//slave

void setup() {
  Serial.begin(9600);
}

void loop() {
  // Send data line 
  for (int i = 0; i < 6; i++) {
    int val = analogRead(A0 + i);
    Serial.print(val);
    if (i < 5) Serial.print(',');
  }
  Serial.println();  // Line 1: data
  
  // Send debug line with # marker 
  for (int i = 0; i < 6; i++) {
    Serial.print("A");
    Serial.print(i);
    Serial.print(":");
    Serial.print(analogRead(A0 + i));
    Serial.print(".C ");
  }
  Serial.println();  // Line 2: Debug info
  
  delay(2000);
}