import RPi.GPIO as GPIO
import time

LED_PIN = 4
LED_YELLOW = 2
LED_GREEN = 3

GPIO.setmode(GPIO.BCM) # GPIO.BCM or GPIO.BOARD
GPIO.setup(LED_PIN, GPIO.OUT) # GPIO.OUT OR GPIO.IN
GPIO.setup(LED_YELLOW, GPIO.OUT)
GPIO.setup(LED_GREEN, GPIO.OUT)

for i in range(1):
    GPIO.output(LED_PIN, GPIO.HIGH) 
    print("red on")
    time.sleep(1) 
    GPIO.output(LED_PIN, GPIO.LOW)
    print("red off")
    time.sleep(1)
    GPIO.output(LED_YELLOW, GPIO.HIGH) 
    print("yellow on")
    time.sleep(1) 
    GPIO.output(LED_YELLOW, GPIO.LOW)
    print("yellow off")
    time.sleep(1)
    GPIO.output(LED_GREEN, GPIO.HIGH) 
    print("green on")
    time.sleep(1) 
    GPIO.output(LED_GREEN, GPIO.LOW)
    print("green off")
    time.sleep(1)
GPIO.cleanup()