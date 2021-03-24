import RPi.GPIO as GPIO
import time
import sys

GPIO.setmode(GPIO.BCM)
pin = 17 # BCM17
GPIO.setup(pin, GPIO.IN)

try:
  while True:
    i = GPIO.input(pin)
    print(i)
    time.sleep(1)

except KeyboardInterrupt:
  GPIO.cleanup()
  sys.exit()

