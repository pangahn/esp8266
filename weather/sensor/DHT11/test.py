from machine import Pin
import time
import dht
import urequests
import ujson

sensor = dht.DHT11(Pin(14))

while True:
  try:
    sensor.measure()
    temperature = sensor.temperature()
    humidity = sensor.humidity()
    data = dict(t=temperature, h=humidity)
    payload = ujson.dumps(data)
    url = 'http://192.168.2.2:1111/'
    response = urequests.post(url, data=payload)
    print('Temperature: {:3.1f} C, Humidity: {:3.1f} %'.format(temperature, humidity))
    time.sleep(59)
  except OSError as e:
    print('Failed to read sensor.')