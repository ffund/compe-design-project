import RPi.GPIO as GPIO
import time
import sys

GPIO.setmode(GPIO.BCM) 
pin = 17 # BCM17
GPIO.setup(pin, GPIO.OUT)
 
try:
  while True:
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(0.005)
    GPIO.output(pin, GPIO.LOW)
    time.sleep(0.005)

except KeyboardInterrupt:
  GPIO.output(pin, GPIO.LOW)
  GPIO.cleanup()
  sys.exit()

