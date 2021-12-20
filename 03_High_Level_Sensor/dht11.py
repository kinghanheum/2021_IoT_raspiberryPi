import Adafruit_DHT

sensor = Adafruit_DHT.DHT11
DHT_PIM = 4

try:
    while True:
        h, t = Adafruit_DHT.ready_retry(sensor, DHT_PIM)
        if h is not None and t is not None:
            print('temperature=%.1f*', Humidity='%.1f%%' % (t, h))
        else: 
            print('Read error')
finally:
    print('ㅂㅇ')
