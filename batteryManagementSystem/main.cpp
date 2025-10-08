// C++ code
//my fucking arch nemesis
// Battery Monitoring System for Arduino

class Battery {
  public:
    float voltage;      // Battery voltage
    float current;      // Battery current
    float temperature;  // Battery temperature
    float soc;          // State of Charge (percentage)

    Battery() {
      voltage = 0.0;
      current = 0.0;
      temperature = 0.0;
      soc = 0.0;
    }

    float calculate_soc() {
      const float max_voltage = 504.0;  // Maximum voltage for a full battery
      soc = (voltage / max_voltage) * 100.0;
      return soc;
    }
};

// Function prototypes
float read_voltage();
float read_current();
float read_temperature();

Battery battery;

void setup() {
  Serial.begin(9600);
}

void loop() {
  // Read battery parameters
  battery.voltage = read_voltage();
  battery.current = read_current();
  battery.temperature = read_temperature();

  // Update State of Charge
  battery.calculate_soc();

  // Display battery status
  Serial.print("Remaining Battery: ");
  Serial.print(battery.soc, 2);
  Serial.println("%");

  // Battery status messages
  if (battery.soc < 20.0) {
    Serial.println("Battery is Low. Please Recharge.");
  } 
  else if (battery.temperature > 60.0) {
    Serial.println("Battery Temperature is too high. Please cool down.");
  } 
  else if (battery.temperature < -20.0) {
    Serial.println("Battery Temperature is too cold. Please warm batteries.");
  } 
  else {
    Serial.println("Battery is in normal condition.");
  }
  Serial.println("----------------------------");

  delay(10000); // Delay for readability (10 seconds)
}

// Example sensor reading functions
float read_voltage() {
  // Replace with actual analogRead and scaling
  return 210.5;  // Dummy value
}

float read_current() {
  // Replace with actual sensor logic
  return 30.0;   // Dummy value
}

float read_temperature() {
  // Replace with actual temperature sensor logic
  return 40.0;   // Dummy value 
}


