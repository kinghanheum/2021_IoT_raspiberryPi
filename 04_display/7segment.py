import RPi.GPIO as GPIO
import time

#               A  B  C  D  E  F  G
SEGMENT_PINS = [14, 15, 16, 17, 18, 19, 20]

GPIO.setmode(GPIO.BCM)

for segment in SEGMENT_PINS:
    GPIO.setup(segment, GPIO.OUT)
    GPIO.output(segment, GPIO.LOW)

data = [1, 1, 1, 1, 1, 1, 0]

try:
    for _ in range(3):
        for i in range(7):
            GPIO.output(SEGMENT_PINS[i], data[i])
        
        time.sleep(1)

        for i in range(7):
            GPIO.output(SEGMENT_PINS[i], GPIO.LOW)

        time.sleep(1)

finally:
    GPIO.cleanup()
    print('ㅂㅇ')