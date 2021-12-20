import RPi.GPIO as GPIO
import time

RED_LED_PIN = 2
YELLOW_LED_PIN = 3
GREEN_LED_PIN = 4

SWITCH_PIN_1 = 10
SWITCH_PIN_2 = 11
SWITCH_PIN_3 = 12

GPIO.setmode(GPIO.BCM)
GPIO.setup(RED_LED_PIN, GPIO.OUT)
GPIO.setup(YELLOW_LED_PIN, GPIO.OUT)
GPIO.setup(GREEN_LED_PIN, GPIO.OUT)

#GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(SWITCH_PIN_1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SWITCH_PIN_2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SWITCH_PIN_3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
    while True:
        val_1 = GPIO.input(SWITCH_PIN_1)
        val_2 = GPIO.input(SWITCH_PIN_2)
        val_3 = GPIO.input(SWITCH_PIN_3)
        time.sleep(0.1)
        GPIO.output(RED_LED_PIN, val_1)
        GPIO.output(YELLOW_LED_PIN, val_2)
        GPIO.output(GREEN_LED_PIN, val_3)
finally:
    GPIO.cleanup()
    print('cleanup and exit')