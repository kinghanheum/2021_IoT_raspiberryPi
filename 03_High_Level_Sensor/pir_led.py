import RPi.GPIO as GPIO
import time

LED_PIN = 2
PIR_PIN = 4
BUZZER_PIN = 21
SEGMENT_PINS = [14, 15, 16, 17, 18, 19, 20]
SEGMENT_PINS_10 = [5, 6, 7, 8, 9, 10, 11]
a=0
sec=0

data=[[1,1,1,1,1,1,0],
      [0,1,1,0,0,0,0],
      [1,1,0,1,1,0,1],
      [1,1,1,1,0,0,1],
      [0,1,1,0,0,1,1],
      [1,0,1,1,0,1,1],
      [1,0,1,1,1,1,1],
      [1,1,1,0,0,0,0],
      [1,1,1,1,1,1,1],
      [1,1,1,0,0,1,1]]

GPIO.setmode(GPIO.BCM)
for segment in SEGMENT_PINS:
    GPIO.setup(segment, GPIO.OUT)
    GPIO.output(segment, GPIO.LOW)
for segment in SEGMENT_PINS_10:
    GPIO.setup(segment, GPIO.OUT)
    GPIO.output(segment, GPIO.LOW)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(PIR_PIN, GPIO.IN)
GPIO.setup(BUZZER_PIN, GPIO.OUT)
pwm = GPIO.PWM(BUZZER_PIN, 262)

time.sleep(5)
print('PIR ready..')

try:
    GPIO.output(LED_PIN, GPIO.LOW)
    while True:
        val = GPIO.input(PIR_PIN)
        if val == GPIO.HIGH :
            print("인식됨")
            a=a+1
            print(a)
            print(sec)
            sec=0
            pwm.stop()
            for i in range(7):
                GPIO.output(SEGMENT_PINS[i], data[a%10][i])
            for i in range(7):
                GPIO.output(SEGMENT_PINS_10[i], data[a//10][i])
            if a>=10: 
                GPIO.output(LED_PIN, GPIO.HIGH)
        else:
            print("인식 안됨")
            
            sec=sec+1
            if(sec>=10): pwm.start(60)
        time.sleep(1)
finally:
    GPIO.cleanup()
    print('cleanup and exit')