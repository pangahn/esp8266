from machine import Pin, PWM
import time
pwm0 = PWM(Pin(9))

pwm0.freq(1)
pwm0.duty(1000)

time.sleep(3)
pwm0.deinit()