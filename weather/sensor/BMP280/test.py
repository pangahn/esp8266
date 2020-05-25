from machine import I2C, Pin
import time
from bmp280 import BMP280

bus = I2C(scl=Pin(2), sda=Pin(0))
bmp = BMP280(bus)
print(bmp.get())