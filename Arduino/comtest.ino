const int sensorpin = A0;
int data;
int time = 0;
void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  data = analogRead(sensorpin);  
Serial.println(String(data)+";"+String(time));
delay(1000);
time+=1;
Serial.flush();
}
