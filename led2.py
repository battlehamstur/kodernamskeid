import RPi.GPIO as GPIO
import time
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)
    
while True:

    sleep(0.5)


    print("LED is on")
    
    GPIO.output(21, GPIO.HIGH)
    time.sleep(0.5)
    print("LED is off")
    GPIO.output(21, GPIO.LOW)
