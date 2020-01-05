import RPi.GPIO as GPIO

# each pin has 2 different naming conventions, tutorial uses BCM
GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

# specify that we are sending signal, not getting input signal
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)

print("LIGHTS OFF")

# set voltage to zero, i.e. turn off the lights
GPIO.output(18, GPIO.LOW)
GPIO.output(23, GPIO.LOW)
GPIO.output(24, GPIO.LOW)

# reset the state of any GPIO pins
GPIO.cleanup()
