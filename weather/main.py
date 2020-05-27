import network, webrepl

wlan = network.WLAN(network.STA_IF)
if not wlan.isconnected():
    print('\nConnecting to network...')
    wlan.active(True)
    wlan.connect('SSID', 'PASSWD')
    while not wlan.isconnected():
        pass
print('Network config:', wlan.ifconfig())
webrepl.start()