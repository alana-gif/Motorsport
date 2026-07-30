//master

const int GREEN_LED  = 9;
const int RED_LED    = 8;
const int TEMP_LIMIT = 700;

int values[6];  

void setup() {
  Serial.begin(9600);

  pinMode(GREEN_LED, OUTPUT);
  pinMode(RED_LED, OUTPUT);

  digitalWrite(GREEN_LED, HIGH);
  digitalWrite(RED_LED, LOW);
  
  // Serial.println("Master ready. Waiting for values...");
}

void loop() {
  static byte index = 0;
  static char buffer[64];

  while (Serial.available()) {
    char c = Serial.read();

    if (c == '\n') {
      buffer[index] = '\0';
      index = 0;

      
      int count = sscanf(
        buffer,
        "%d,%d,%d,%d,%d,%d",  // format specifiers
        &values[0], &values[1], &values[2], 
        &values[3], &values[4], &values[5]
      );

      if (count == 6) {
        bool shutdown = false;

        // Check 6 values
        for (int i = 0; i < 6; i++) {
          if (values[i] > TEMP_LIMIT) {
            shutdown = true;
            break;
          }
        }

        digitalWrite(GREEN_LED, !shutdown);
        digitalWrite(RED_LED, shutdown);

        if (shutdown) {
          Serial.println("SHUTDOWN TRIGGERED");
        }
        
        // Optional: print received values
        // Serial.print("Received: ");
        // for (int i = 0; i < 6; i++) {
        //   Serial.print(values[i]);
        //   if (i < 5) Serial.print(",");
        // }
        // Serial.println();
      }
      // else {
      //   Serial.print("Parse error. Expected 6, got ");
      //   Serial.print(count);
      //   Serial.print(" values. Buffer: ");
      //   Serial.println(buffer);
      // }
    }
    else if (index < sizeof(buffer) - 1) {
      buffer[index++] = c;
    }
  }
}