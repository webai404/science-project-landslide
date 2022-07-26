void setup() {
  // 初始化與樹莓派之間的聯繫
  Serial.begin(115200);
  // 初始化腳位
  pinMode(3, INPUT); // 水銀
  pinMode(A0, INPUT); // 光纖
  pinMode(A2, INPUT); // 光敏電阻
  pinMode(A3, INPUT); // 雨量
  pinMode(5, OUTPUT); // 自動開關燈
  pinMode(6, OUTPUT); // 雨量偵測警示燈
}
void loop() {
  // 把數據傳給樹莓派統整
  Serial.print(digitalRead(3));
  Serial.print(" ");
  Serial.print(analogRead(A0));
  Serial.print(" ");
  Serial.print(analogRead(A3));

  // 雨量警示燈
  if (analogRead(A3) < 400) {
    digitalWrite(5, LOW);
  }

  else {
    digitalWrite(5, HIGH);
  }

  // 自動開關燈
  if (analogRead(A2) < 215) {
    digitalWrite(5, LOW);
  }

  else {
    digitalWrite(5, HIGH);
  }
}
