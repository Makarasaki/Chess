class Motor {
  public:
    unsigned int step_pin;
    unsigned int dir_pin;
    unsigned int endstop_pin;
    unsigned int step_resolution;
    unsigned int enable_pin;
    int dir;
    long delta;
    int home_dir;
    bool is_step;


    Motor(unsigned int step_pin, unsigned int dir_pin, unsigned int enable_pin, unsigned int endstop_pin, float step_resolution, int home_dir) {
      this->step_pin = step_pin;
      this->dir_pin = dir_pin;
      this->step_resolution = step_resolution;
      this->enable_pin = enable_pin;
      this->endstop_pin = endstop_pin;
      this-> dir = 0;
      this-> delta = 0;
      this-> is_step = 0;
      this-> home_dir = home_dir;

      pinMode(this->step_pin, OUTPUT);
      pinMode(this->dir_pin,  OUTPUT);
      pinMode(this->enable_pin,  OUTPUT);
      pinMode(this->endstop_pin,  INPUT_PULLUP);
      digitalWrite(this->enable_pin, LOW);
    }

    int home() {
      int delay = 300;
      digitalWrite(this->dir_pin, home_dir);
      while (digitalRead(this->endstop_pin)) {

        digitalWrite(this->step_pin, HIGH);
        delayMicroseconds(delay);
        digitalWrite(this->step_pin, LOW);
        delayMicroseconds(delay);
      }
      digitalWrite(this->dir_pin, ((home_dir > 0) ? LOW : HIGH));
      while (!(digitalRead(this->endstop_pin))) {

        digitalWrite(this->step_pin, HIGH);
        delayMicroseconds(delay);
        digitalWrite(this->step_pin, LOW);
        delayMicroseconds(delay);
      }
      
      digitalWrite(this->dir_pin, home_dir);
      while (digitalRead(this->endstop_pin)) {

        digitalWrite(this->step_pin, HIGH);
        delayMicroseconds(delay);
        digitalWrite(this->step_pin, LOW);
        delayMicroseconds(delay);
      }
      return 0;
    }
};
