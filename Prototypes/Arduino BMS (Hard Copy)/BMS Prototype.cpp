// Prototype BMS Simulator 20/05/26
// Now Includes thermal kill function 22/05/26

const int voltagePin = A0;
const int tempPin = A1;

float batteryVoltage;
float batteryPercent;
float temperature;

bool systemKilled = false;

void setup() {
  Serial.begin(9600);

  Serial.println("BMS Prototype Started");
  Serial.println("----------------------");
}

void loop() {

  // Stop everything if system killed
  if (systemKilled) {
    return;
  }

  // ----------------------------
  // Battery Voltage
  // ----------------------------

  int rawVoltage = analogRead(voltagePin);

  // Simulate battery range 0V–16.8V
  batteryVoltage =
      (rawVoltage / 1023.0) * 16.8;

  // Battery percentage
  batteryPercent =
      (batteryVoltage / 16.8) * 100;

  batteryPercent =
      constrain(batteryPercent, 0, 100);

  // // ----------------------------
  // // Temperature
  // // ----------------------------

  int rawTemp = analogRead(tempPin);

  // Simulated 0–100°C
  temperature =
      (rawTemp / 1023.0) * 100;

  // ----------------------------
  // Output Data
  // ----------------------------

  Serial.print("Battery Voltage: ");
  Serial.print(batteryVoltage);
  Serial.println(" V");

  Serial.print("Battery Level: ");
  Serial.print(batteryPercent);
  Serial.println(" %");

  Serial.print("Temperature: ");
  Serial.print(temperature);
  Serial.println(" C");

  // ----------------------------
  // Safety Warnings
  // ----------------------------

  if (batteryVoltage < 12.0) {
    Serial.println("WARNING: LOW BATTERY");
  }

  // ----------------------------
  // THERMAL KILL FUNCTION
  // ----------------------------

  if (temperature > 60) {

    Serial.println("CRITICAL WARNING: OVERHEATING");
    Serial.println("SYSTEM SHUTDOWN ACTIVATED");
    Serial.println("RESET ARDUINO TO RESTART");

    systemKilled = true;

    while (true) {
      // Freeze program forever
    }
  }

  Serial.println("----------------------");

  delay(1000);
}

//instructions
//pot 1 is the pretend battery voltage
//pot 1 is also repsonsible for doing the math to calculate the SOC
//pot 2 is the pretend battery tempreture
//added kill function. should all be good
//this doc seems to only want to work with the potentiometrs.
