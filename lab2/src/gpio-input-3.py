import RPi.GPIO as GPIO
import time
import sys

GPIO.setmode(GPIO.BCM) 
pin = 17 # BCM17
GPIO.setup(pin, GPIO.IN)
 
def callback_fn(input_pin): 
  print("Button press on pin", input_pin)

GPIO.add_event_detect(pin, 
  GPIO.FALLING,  
  callback=callback_fn)

try:
  while True:
    print("Hello!")
    time.sleep(1)
except KeyboardInterrupt:
  GPIO.cleanup()
  sys.exit()

