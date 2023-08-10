#include "Motor.h"
#include <Servo.h>

#define servo_pin 11
#define servo_up 85
#define servo_down 180
#define speed_with_figure 50
#define speed_without_figure 30
#define servo_delay 500
#define done 1

Motor motor[2] = {Motor(2, 5, 8, 9, 5 * 32, 1), Motor(3, 6, 8, 10, 5 * 32, 1)};

float poz_X = 0;
float poz_Y = 0;
int step_delay = speed_without_figure;

Servo servo;


void setup() {
  Serial.begin(115200);
  servo.attach(servo_pin);
  servo.write(servo_down);
}
void loop() {
  if (Serial.available() > 0) {
    String message = Serial.readStringUntil("\n");
    char message_ch[message.length()];
    message.toCharArray(message_ch, message.length());
    if (mode('H', -1, message_ch) == 1) {
      servo.write(servo_down);
      poz_X = motor[0].home();
      poz_Y = motor[1].home();
    } else {
      line(mode('X', poz_X, message_ch), mode('Y', poz_Y, message_ch), mode('M', 0, message_ch));
    }
    Serial.println(done);
  }
}


float mode(char litera, float zwrot, char linijka[]) {
  char *ptr = linijka;
  for (int i = 0; i < 5; i++) {
    if (*ptr == litera) {
      return atof(ptr + 1);
    } else {
      ptr = strchr(ptr, ' ') + 1;
    }
  }
  return zwrot;
}

void line(float NN_poz_X, float NN_poz_Y, float magnet_poz) {
  if (magnet_poz == 0 and servo.read() != servo_down) {
    servo.write(servo_down);
    delay(servo_delay);
    step_delay = speed_without_figure;
  } else if (magnet_poz == 1 and servo.read() != servo_up) {
    servo.write(servo_up );
    delay(servo_delay);
    step_delay = speed_with_figure;
  }
  motor[0].delta = round((poz_X - NN_poz_X) * motor[0].step_resolution);
  motor[0].delta = abs(motor[0].delta);
  motor[0].dir = (poz_X > NN_poz_X) ? HIGH : LOW;
  digitalWrite(motor[0].dir_pin, motor[0].dir);
  motor[1].delta = round((poz_Y - NN_poz_Y) * motor[1].step_resolution);
  motor[1].delta = abs(motor[1].delta);
  motor[1].dir = (poz_Y > NN_poz_Y) ? HIGH : LOW;
  digitalWrite(motor[1].dir_pin, motor[1].dir);
long Max;
  if (motor[0].delta > motor[1].delta) {
    Max = motor[0].delta;
  } else {
    Max = motor[1].delta;
  }
  long i = Max;
  long Xpom = Max / 2;
  long Ypom = Max / 2;

  for (;;) {
    if (i-- <= 0) break;

    Xpom -= motor[0].delta;
    if (Xpom < 0) {
      Xpom += Max;
      motor[0].is_step = 1;
    }

    Ypom -= motor[1].delta;
    if (Ypom < 0 ) {
      Ypom += Max;
      motor[1].is_step = 1;
    }

    (motor[0].is_step == 1) ? digitalWrite(motor[0].step_pin, HIGH) : digitalWrite(motor[0].step_pin, LOW);
    (motor[1].is_step == 1) ? digitalWrite(motor[1].step_pin, HIGH) : digitalWrite(motor[1].step_pin, LOW);

    delayMicroseconds(step_delay);
    digitalWrite(motor[0].step_pin, LOW);
    digitalWrite(motor[1].step_pin, LOW);
    delayMicroseconds(step_delay);

    motor[0].is_step = 0;
    motor[1].is_step = 0;

  }

  poz_X = NN_poz_X;
  poz_Y = NN_poz_Y;
}
