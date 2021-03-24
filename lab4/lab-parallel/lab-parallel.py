import RPi.GPIO as GPIO
import time

# GPIO pin to LCD pin mapping
LCD_RS = 6
LCD_E  = 5
LCD_D4 = 22
LCD_D5 = 23
LCD_D6 = 24
LCD_D7 = 25

# Define state of RS pin in character and command mode
LCD_CHR = GPIO.HIGH   # High in data (character) mode
LCD_CMD = GPIO.LOW    # Low in instruction (command) mode

# Addresses of each line of the display
LCD_LINE_1 = 0b10000000
LCD_LINE_2 = 0b11000000

# Timing constants
E_PULSE = 0.0005
E_DELAY = 0.0005

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)       # Use BCM GPIO numbers

def int_to_arr(i):
     return [int(b) for b in format(i, '08b')]

def char_to_arr(c):
  return [int(b) for b in format(ord(c), '08b')]

def write_arr_4bit(bits, mode, debug=True):

  pins = [LCD_D7, LCD_D6, LCD_D5, LCD_D4]

  GPIO.output(LCD_RS, mode) # RS - command or character mode

  # set most significant bits (high bits) on data lines
  for p, b in zip(pins, bits[:4]):
    GPIO.setup(p, GPIO.OUT)
    GPIO.output(p, b)

  # pulse clock
  time.sleep(E_DELAY)
  GPIO.output(LCD_E, GPIO.HIGH)
  time.sleep(E_PULSE)
  GPIO.output(LCD_E, GPIO.LOW)
  time.sleep(E_DELAY)

  # set least significant bits on data lines
  for p, b in zip(pins, bits[4:]):
    GPIO.setup(p, GPIO.OUT)
    GPIO.output(p, b)

  # pulse clock
  time.sleep(E_DELAY)
  GPIO.output(LCD_E, GPIO.HIGH)
  time.sleep(E_PULSE)
  GPIO.output(LCD_E, GPIO.LOW)
  time.sleep(E_DELAY)

  # reset pins to 0
  for p in pins:
    GPIO.output(p, GPIO.LOW)

def string_to_lcd(s):
    write_arr_4bit(int_to_arr(LCD_LINE_1), LCD_CMD)
    for c in s:
        write_arr_4bit(char_to_arr(c), LCD_CHR)

def setup():

    GPIO.setup(LCD_E, GPIO.OUT)  # E
    GPIO.setup(LCD_RS, GPIO.OUT) # RS

    pins = [LCD_D7, LCD_D6, LCD_D5, LCD_D4]
    for p in pins:
        GPIO.setup(p, GPIO.OUT)

    write_arr_4bit(int_to_arr(0b00110011), LCD_CMD)
    write_arr_4bit(int_to_arr(0b00110010), LCD_CMD)
    write_arr_4bit(int_to_arr(0b00001100), LCD_CMD)
    write_arr_4bit(int_to_arr(0b00000001), LCD_CMD)

    print("All peripherals and sensors have been set up successfully!")
    return True


setup()
time.sleep(5)
string_to_lcd('U')
time.sleep(60)
