import network, webrepl
# from sensor import jobs

wlan = network.WLAN(network.STA_IF)
if not wlan.isconnected():
    print('\nConnecting to network...')
    wlan.active(True)
    wlan.connect('', '')
    while not wlan.isconnected():
        pass
print('Network config:', wlan.ifconfig())
webrepl.start()
# jobs(60, 5)