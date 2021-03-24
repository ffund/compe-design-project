import RPi.GPIO as GPIO
import time
import sys

GPIO.setmode(GPIO.BCM)

DATA = [5, 6, 7, 8, 9, 10, 11, 12]
CLK = 18

def arr_to_char(a):
  bitstr = ''.join(str(b) for b in a)
  c = format(int(bitstr, 2), 'c')
  return c


def read_char(pins, clk, debug=True):
  bits = []
  GPIO.setup(clk, GPIO.IN)
  GPIO.wait_for_edge(clk, GPIO.FALLING)
  for p in pins:
    GPIO.setup(p, GPIO.IN)
    b = GPIO.input(p)
    bits.append(b)
  if debug:
    print(bits)

  return (arr_to_char(bits))

def read_char_4bit(pins, clk, debug=True):
  bits = []
  GPIO.setup(clk, GPIO.IN)
  GPIO.wait_for_edge(clk, GPIO.FALLING)

  for p in pins:
    GPIO.setup(p, GPIO.IN)
    b = GPIO.input(p)
    bits.append(b)

  GPIO.wait_for_edge(clk, GPIO.FALLING)

  for p in pins:
    GPIO.setup(p, GPIO.IN)
    b = GPIO.input(p)
    bits.append(b)

  if debug:
    print(bits)

  return (arr_to_char(bits))

try:
  while True:
    c = read_char_4bit(DATA[4:], CLK)
    print(c)

except KeyboardInterrupt:
  GPIO.cleanup()
  sys.exit()
