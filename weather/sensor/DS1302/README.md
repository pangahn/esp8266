# [Micorpython DS1302 RTC Clock Driver](https://github.com/omarbenhamid/micropython-ds1302-rtc)
This is a pure Micropython DS1302 RTC Clock driver. This is based on microbit code of [microbit-lib](https://github.com/shaoziyang/microbit-lib).

This has been tested and working on ESP32 but should work with any micropython supported device.

# Dirver documentation

## API

* **start()**  
start RTC.  

* **stop()**  
stop/pause RTC

* **DateTime(DT = None)**  
get / set DateTime. If no paramter given, it will return current datetime, otherwise it will set datatime.  
datatime format: [Year, month, day, weekday, hour, minute, second]

* **Year(year = None)**  
get / set year.  

* **Month(month = None)**  
get / set month.  

* **Day(day = None)**  
get / set day.  

* **Weekday(weekday = None)**  
get / set month.  

* **Hour(hour = None)**  
get / set hour.  

* **Minute(minute = None)**  
get / set minute.  

* **Second(second = None)**  
get / set second.  

* **ram(reg, dat = None)**  
get / set ram data (31 bytes).  


## Example

```
from machine import Pin
import DS1302
import time

# CLK, DAT, RST
ds = DS1302.DS1302(Pin(14), Pin(12), Pin(13))
ds.DateTime([2020, 5, 8, 5, 18, 50, 10])

while True:
    print(ds.DateTime())
    time.sleep(5)
```
