import random
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
pin = 17 # BCM17


def setup():
    GPIO.setup(pin, GPIO.OUT)
    print("All peripherals and sensors have been set up successfully!")
    return True

def led_on():
    GPIO.output(pin, GPIO.HIGH)
    print("The LED is ON")

def led_off():
    GPIO.output(pin, GPIO.LOW)
    print("The LED is OFF")

def read_light_level():
    return random.randint(50,70)
