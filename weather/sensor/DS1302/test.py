from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import DS1302
import time

ds = DS1302.DS1302(Pin(4),Pin(5),Pin(16))
i2c = I2C(scl=Pin(13), sda=Pin(12))

oled = SSD1306_I2C(128, 64, i2c)
oled.text('Hello', 0, 0)
oled.show()

#ds.DateTime([2020, 5, 15, 5, 20, 52, 55])

while True:
    date = ds.DateTime()
    date = [str(i) for i in date]
    s1 = '{}-{}-{}'.format(date[0], date[1], date[2])
    s2 = '{}:{}:{}'.format(date[4], date[5], date[6])
    oled.fill(0)
    oled.text(s1, 0, 0)
    oled.text(s2, 0, 10)
    oled.show()
    time.sleep(5)