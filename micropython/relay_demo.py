from machine import Pin
import time

relay = Pin(16, Pin.OUT)
while True:
    relay.on()
    time.sleep(1)
    relay.off()
    time.sleep(1)