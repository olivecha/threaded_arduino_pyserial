void setup() {
  Serial.begin(115200); // use the same baud-rate as the python side
}
void loop() {

  // read value from analog pin
  int sensorValue0 = analogRead(A0);
  float voltage0 = sensorValue0 * ( 5.0 / 1023.0 );

  Serial.println(voltage0);
}
