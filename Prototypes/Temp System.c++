// C++ code
// Battery Monitoring System for Arduino
//mwahahahahaha

#define RED 4
#define BLUE 7
#define GREEN 8


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
      const float max_voltage = 360.0;  // Maximum voltage for a full battery
      soc = (voltage / max_voltage) * 100.0;
      return soc;
    }
};

// writes to led pins between 0 low to 255 high 
// give rgb vals for each one (r, g, b)
void changeLed(int red, int green, int blue){
 	analogWrite(RED, red);
    analogWrite(GREEN, green);
    analogWrite(BLUE, blue);
}

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

  // Print temperature reading
  Serial.print("Battery Temperature: ");
  Serial.print(battery.temperature, 2);
  Serial.println(" °C");

  // Update State of Charge
  battery.calculate_soc();

  // Display battery status
  Serial.print("Remaining Battery: ");
  Serial.print(battery.soc, 2);
  Serial.println("%");

  // Voltage check (ADDED FEATURE)
  if (battery.voltage > 360.0) {
    Serial.println("VOLTAGE TOO HIGH, CUT CIRCUIT");
    changeLed(255,0,0);
    while(true){
      Serial.println("circuit cut");
    	delay(10000);
    }
  }
  
  // Current check (ADDED FEATURE)
  if (battery.current > 50.0) { // Example max current threshold
    Serial.println("CURRENT TOO HIGH, CUT CIRCUIT");
    changeLed(255,0,0);
    while(true){
      Serial.println("circuit cut");
    	delay(10000);
    }
  }

  // Battery status messages
  if (battery.soc < 20.0) {
    Serial.println("Battery is Low. Please Recharge.");
    changeLed(255,255,0);
  } 
    else if (battery.temperature > 60.0) {
    Serial.println("Battery Temperature is too high. shutting down");
    changeLed(255,0,0);
    while(true){
      Serial.println("circuit cut");
    	delay(10000);
      }
  } 
  else if (battery.temperature > 50.0) {
    Serial.println("Battery Temperature is too high. Please cool down.");
        changeLed(255,255,0);
  } 
  else if (battery.temperature < -20.0) {
    Serial.println("Battery Temperature is too cold. Please warm batteries.");
        changeLed(255,255,0);
  } 
  else {
    Serial.println("Battery is in normal condition.");
        changeLed(0,255,0);
  }

  Serial.println("----------------------------");

  delay(2000); // Delay for readability (2 seconds)
}

// Example sensor reading functions
float read_voltage() {
  int raw = analogRead(A0); // analogRead() max 1023 so when divided by
  // 1023 it will return between 0 and 1 
  return (raw / 1023.0) * 500.0; // example: 578 / 1023 = 0.56500489 * 500 = 282.50244379
}

float read_current() {
  int raw = analogRead(A1);
  return (raw / 1023.0) * 60.0; // max current = 60A
}

float read_temperature() {
  int raw = analogRead(A2);
  return (raw / 1023.0) * 100.0 - 25.0; // example: range -25°C to 75°C
}

#hello