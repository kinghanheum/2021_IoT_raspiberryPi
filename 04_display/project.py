import RPi.GPIO as GPIO
import time

SWITCH_PIN_1 = 2
SWITCH_PIN_2 = 3
PRI_PIN = 4
BUZZER_PIN = 21
SEGMENT_PINS = [14, 15, 16, 17, 18, 19, 20]

GPIO.setmode(GPIO.BCM)
GPIO.setup(SWITCH_PIN_2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
    while True:
        val_1 = GPIO.input(SWITCH_PIN_2)
        print(val_1)
        time.sleep(0.1)

finally:
    GPIO.cleanup()
    print("cleanup")