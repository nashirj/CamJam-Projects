# This program blinks the LED a finite number of times

import time
import RPi.GPIO as GPIO

# each pin has 2 different naming conventions, tutorials use BCM
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set pins for output 
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)

while True:
    print("LIGHTS ON")
    # set voltage to high, i.e. turn on the lights
    GPIO.output(18, GPIO.HIGH)
    GPIO.output(23, GPIO.HIGH)
    GPIO.output(24, GPIO.HIGH)

    time.sleep(1)

    print("LIGHTS OFF")
    GPIO.output(18, GPIO.LOW)
    GPIO.output(23, GPIO.LOW)
    GPIO.output(24, GPIO.LOW)

    time.sleep(1)
