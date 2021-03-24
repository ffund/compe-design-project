import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

DATA = [5, 6, 7, 8, 9, 10, 11, 12]
CLK = 18
PULSE_LOW = 0.001
PULSE_HIGH = 0.001

def char_to_arr(c):
  return [int(b) for b in format(ord(c), '08b')]

def write_char(c, pins, clk, debug=True):
  GPIO.setup(clk, GPIO.OUT)
  GPIO.output(clk, GPIO.LOW)
  bits = char_to_arr(c)
  if debug:
    print(bits)
  # set bits on data lines
  for p, b in zip(pins, bits):
    GPIO.setup(p, GPIO.OUT)
    GPIO.output(p, b)

  # pulse clock (rx on falling edge)
  GPIO.output(clk, GPIO.HIGH)
  time.sleep(PULSE_HIGH)
  GPIO.output(clk, GPIO.LOW)
  time.sleep(PULSE_LOW)

  # reset pins to 0
  for p in pins:
    GPIO.output(p, GPIO.LOW)

def write_char_4bit(c, pins, clk, debug=True):
  GPIO.setup(clk, GPIO.OUT)
  GPIO.output(clk, GPIO.LOW)
  bits = char_to_arr(c)
  if debug:
    print(bits)

  # set most significant bits on data lines
  for p, b in zip(pins, bits[:4]):
    GPIO.setup(p, GPIO.OUT)
    GPIO.output(p, b)

  # pulse clock (rx on falling edge)
  GPIO.output(clk, GPIO.HIGH)
  time.sleep(PULSE_HIGH)
  GPIO.output(clk, GPIO.LOW)
  time.sleep(PULSE_LOW)

  # set least significant bits on data lines
  for p, b in zip(pins, bits[4:]):
    GPIO.setup(p, GPIO.OUT)
    GPIO.output(p, b)

  # pulse clock (rx on falling edge)
  GPIO.output(clk, GPIO.HIGH)
  time.sleep(PULSE_HIGH)
  GPIO.output(clk, GPIO.LOW)
  time.sleep(PULSE_LOW)

  # reset pins to 0
  for p in pins:
    GPIO.output(p, GPIO.LOW)


#write_char('H', DATA, CLK, debug=True)
#write_char('e', DATA, CLK, debug=True)
#write_char('l', DATA, CLK, debug=True)
#write_char('l', DATA, CLK, debug=True)
#write_char('o', DATA, CLK, debug=True)

time.sleep(0.005)

write_char_4bit('H', DATA[4:], CLK, debug=True)
write_char_4bit('e', DATA[4:], CLK, debug=True)
write_char_4bit('l', DATA[4:], CLK, debug=True)
write_char_4bit('l', DATA[4:], CLK, debug=True)
write_char_4bit('o', DATA[4:], CLK, debug=True)

