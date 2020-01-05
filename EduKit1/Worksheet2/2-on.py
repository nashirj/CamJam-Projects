import RPi.GPIO as GPIO

# each pin has 2 different naming conventions, tutorial uses BCM
GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

# specify that we are sending signal, not getting input signal
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)

print("LIGHTS ON")

# set voltage to high, i.e. turn on the lights
GPIO.output(18, GPIO.HIGH)
GPIO.output(23, GPIO.HIGH)
GPIO.output(24, GPIO.HIGH)
