from machine import Pin
import urequests
import time
import json


trig_pin = 2
echo_pin = 0

trig = Pin(trig_pin, Pin.OUT)
echo = Pin(echo_pin, Pin.IN)
light = Pin(2, Pin.OUT)


def pin_reset():
    trig.value(0)
    echo.value(0)
    time.sleep(2)


def high_level():
    trig.value(1)
    time.sleep_us(80)
    trig.value(0)


def calculator(duration):
    # 340m/s=34000cm/s=0.0343cm/us
    return (duration * 0.0343 / 2 ) * 1.03


def std(result):
    N = len(result)
    m = sum(result) / N
    tmp = 0
    for s in result:
        tmp = tmp + (s-m) * (s-m)
    return pow(tmp/(N-1), 0.5)


def quick_sort(nums, low, high):
    if low >= high:
        return
    w = partition(nums, low, high)
    quick_sort(nums, low, w - 1)
    quick_sort(nums, w + 1, high)


def partition(nums, low, high):
    i = low
    for j in range(low, high):
        if nums[j] < nums[high]:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    nums[i], nums[high] = nums[high], nums[i]
    return i


def show_status(func):
    def wrapper(*args):
        light.value(0)
        value = func(*args)
        light.value(1)
        return value
    return wrapper


def message(history):
    std_value = std(history)
    quick_sort(history, 0, len(history) - 1)
    history = history[1:-1]
    avg_value = sum(history)/len(history)
    return dict(std=std_value, avg=avg_value)


@show_status
def distance_measure(cycle):
    history = []
    for i in range(cycle):
        pin_reset()
        high_level()

        while(echo.value()==0):
            pass

        pulse_start = time.ticks_us()

        while(echo.value()==1):
            pass

        pulse_end = time.ticks_us()
        dist = calculator(pulse_end - pulse_start)
        print('{}--->{}'.format(i, dist))
        history.append(dist)
    return history


def sender(msg):
    text = '{}'.format(msg['avg'], msg['std'])
    description = '%e6%a0%a1%e6%ad%a3%e5%90%8e%e5%9d%87%e5%80%bc%e4%b8%ba%ef%bc%9a{}cm.%0d%0a%0d%0a%e5%8e%9f%e5%a7%8b%e6%a0%87%e5%87%86%e5%b7%ae%e4%b8%ba%ef%bc%9a{}cm.'.format(msg['avg'], msg['std'])
    SCKEY = ''
    url = 'https://sc.ftqq.com/{}.send?text={}&desp={}'.format(SCKEY, text, description)
    print(text)
    print(url)
    headers = {'Content-type': 'application/x-www-form-urlencoded'}
    response = urequests.get(url, headers=headers)
    return response.json()['errmsg']


def jobs(period, cycle):
    while True:
        history = distance_measure(cycle)
        msg = message(history)
        err_msg = sender(msg)
        print(err_msg)
        time.sleep(period)