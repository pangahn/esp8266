from machine import Pin, I2C
i2c = I2C(scl=Pin(16), sda=Pin(5))

from ssd1306 import SSD1306_I2C
oled = SSD1306_I2C(128, 64, i2c)

oled.text('Hello', 0, 0)
oled.text('World', 0, 10)
oled.show()