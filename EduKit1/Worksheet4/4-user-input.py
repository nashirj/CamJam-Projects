# Use user input to blink an LED

import os
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

LED_red = 18
LED_yellow = 23
LED_green = 24

GPIO.setup(LED_red, GPIO.OUT)
GPIO.setup(LED_yellow, GPIO.OUT)
GPIO.setup(LED_green, GPIO.OUT)

os.system('clear')

# Ask user which LED to blink
print("Which LED would you like to blink?")
print("1: Red")
print("2: Yellow")
print("3: Green")

led_choice = None
while led_choice is None:
    try:
        led_choice = int(input("Pick an option (1, 2, or 3): "))
    except ValueError:
        print("Please enter an integer")
        exit()

count = None
while count is None:
    try:
        count = int(input("How many times would you like the LED to blink? "))
    except ValueError:
        print("Please enter an integer")
        exit()

print "You picked the",
if led_choice == 1:
    print "red",
    led_choice = LED_red 
elif led_choice == 2:
    print "yellow",
    led_choice = LED_yellow
elif led_choice == 3:
    print "green",
    led_choice = LED_green
print "LED."

while count > 0:
    GPIO.output(led_choice, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(led_choice, GPIO.LOW)
    time.sleep(1)
    count -= 1

GPIO.cleanup()

