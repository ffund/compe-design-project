import RPi.GPIO as GPIO
import time
import sys

GPIO.setmode(GPIO.BCM)
pin = 17 # BCM17
GPIO.setup(pin, GPIO.IN)

try:
  GPIO.wait_for_edge(pin, GPIO.FALLING)
  print("Button is pressed")
  sys.exit()

except KeyboardInterrupt:
  GPIO.cleanup()
  sys.exit()


