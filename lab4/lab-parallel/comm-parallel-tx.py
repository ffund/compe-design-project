import RPi.GPIO as GPIO
import time
import sys

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

DATA = [5, 6, 7, 8, 9, 10, 11, 12]
RW = 16
EN = 18

BIT_TIME = 0.005

def char_to_arr(c):
    return [int(b) for b in format(ord(c), '08b')]


# don't forget to:
# set pin to output before and input after
# wait for bit time!
def write_char(c, pins, en, debug=True):
  bits = char_to_arr(c)
  if debug:
    print(bits)
  GPIO.setup(en, GPIO.OUT)
  GPIO.output(en, GPIO.HIGH)
  for p in pins:
    GPIO.setup(p, GPIO.OUT)
  for (p, b) in zip(pins, bits):
    GPIO.output(p, b)
  time.sleep(BIT_TIME/2)
  GPIO.output(en, GPIO.LOW)
  time.sleep(BIT_TIME/2)
  for p in pins:
    GPIO.setup(p, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
  GPIO.setup(en, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def write_char_4bit(c, pins, en, debug=True):
  bits = char_to_arr(c)
  if debug:
    print(bits)
  GPIO.setup(en, GPIO.OUT)
  GPIO.output(en, GPIO.HIGH)
  for p in pins:
    GPIO.setup(p, GPIO.OUT)
  for (p, b) in zip(pins, bits[:4]):
    GPIO.output(p, b)

  time.sleep(BIT_TIME/2)
  GPIO.output(en, GPIO.LOW)
  time.sleep(BIT_TIME/2)

  GPIO.output(en, GPIO.HIGH)
  for (p, b) in zip(pins, bits[4:]):
    GPIO.output(p, b)
  time.sleep(BIT_TIME/2)
  GPIO.output(en, GPIO.LOW)
  time.sleep(BIT_TIME/2)

write_char_4bit('h', DATA[4:], EN, debug=True)
write_char_4bit('e', DATA[4:], EN, debug=True)
write_char_4bit('l', DATA[4:], EN, debug=True)
write_char_4bit('l', DATA[4:], EN, debug=True)
write_char_4bit('o', DATA[4:], EN, debug=True)

