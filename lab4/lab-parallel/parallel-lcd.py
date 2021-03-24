#!/usr/bin/python

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
LCD_CHR = True   # High in data (character) mode
LCD_CMD = False  # Low in instruction (command) mode

# Addresses of each line of the display
LCD_LINE_1 = 0b10000000 
LCD_LINE_2 = 0b11000000 

# Timing constants
E_PULSE = 0.0005
E_DELAY = 0.0005

def main():

  # Main program block
  
  GPIO.setwarnings(False)
  GPIO.setmode(GPIO.BCM)       # Use BCM GPIO numbers

  # Set GPIO pins as output
  GPIO.setup(LCD_E, GPIO.OUT)  # E
  GPIO.setup(LCD_RS, GPIO.OUT) # RS
  GPIO.setup(LCD_D4, GPIO.OUT) # DB4
  GPIO.setup(LCD_D5, GPIO.OUT) # DB5
  GPIO.setup(LCD_D6, GPIO.OUT) # DB6
  GPIO.setup(LCD_D7, GPIO.OUT) # DB7


  # Initialize display
  print("Initializing display")
  lcd_init()

  time.sleep(5)

  print("Writing 'Hello' to line 1")
  #lcd_byte(LCD_LINE_1, LCD_CMD)
  lcd_byte(ord("H"), LCD_CHR) 
  lcd_byte(ord("e"), LCD_CHR)
  lcd_byte(ord("l"), LCD_CHR)
  lcd_byte(ord("l"), LCD_CHR)
  lcd_byte(ord("o"), LCD_CHR)
  lcd_byte(ord("H"), LCD_CHR)
  lcd_byte(ord("e"), LCD_CHR)
  lcd_byte(ord("l"), LCD_CHR)
  lcd_byte(ord("l"), LCD_CHR)
  lcd_byte(ord("o"), LCD_CHR)
  lcd_byte(ord("H"), LCD_CHR)
  lcd_byte(ord("e"), LCD_CHR)
  lcd_byte(ord("l"), LCD_CHR)
  lcd_byte(ord("l"), LCD_CHR)
  lcd_byte(ord("o"), LCD_CHR)
  lcd_byte(ord("H"), LCD_CHR)
  lcd_byte(ord("e"), LCD_CHR)
  lcd_byte(ord("l"), LCD_CHR)
  lcd_byte(ord("l"), LCD_CHR)
  lcd_byte(ord("o"), LCD_CHR)
  lcd_byte(ord("H"), LCD_CHR)
  lcd_byte(ord("e"), LCD_CHR)
  lcd_byte(ord("l"), LCD_CHR)
  lcd_byte(ord("l"), LCD_CHR)
  lcd_byte(ord("o"), LCD_CHR)
  lcd_byte(ord("H"), LCD_CHR)
  lcd_byte(ord("e"), LCD_CHR)
  lcd_byte(ord("l"), LCD_CHR)
  lcd_byte(ord("l"), LCD_CHR)
  lcd_byte(ord("o"), LCD_CHR)
  lcd_byte(ord("H"), LCD_CHR)
  lcd_byte(ord("e"), LCD_CHR)
  lcd_byte(ord("l"), LCD_CHR)
  lcd_byte(ord("l"), LCD_CHR)
  lcd_byte(ord("o"), LCD_CHR)
  lcd_byte(ord("H"), LCD_CHR)
  lcd_byte(ord("e"), LCD_CHR)
  lcd_byte(ord("l"), LCD_CHR)
  lcd_byte(ord("l"), LCD_CHR)
  lcd_byte(ord("o"), LCD_CHR)
  lcd_byte(ord("H"), LCD_CHR)
  lcd_byte(ord("e"), LCD_CHR)
  lcd_byte(ord("l"), LCD_CHR)
  lcd_byte(ord("l"), LCD_CHR)
  lcd_byte(ord("o"), LCD_CHR)
  lcd_byte(ord("H"), LCD_CHR)
  lcd_byte(ord("e"), LCD_CHR)
  lcd_byte(ord("l"), LCD_CHR)
  lcd_byte(ord("l"), LCD_CHR)
  lcd_byte(ord("o"), LCD_CHR)

  time.sleep(60)

def lcd_init():

  # Initialize display as described in datasheet
  lcd_byte(0b00110011,LCD_CMD) # 0011 0011 
  lcd_byte(0b00110010,LCD_CMD) # 0011 0010 - now in 4-bit mode

  #lcd_byte(0b00001100,LCD_CMD) # 0000 1000 Display on - 5.2.4 in datasheet
  lcd_byte(0b00001110, LCD_CMD) # display on with cursor - see page 42, table 12
  lcd_byte(0b00000110, LCD_CMD) # entry mode set
  #lcd_byte(0b00000001,LCD_CMD) # 0000 0001 Clear display - 5.2.1 in datasheet


# Function for sending one byte of data to the display
# Takes care of setting the RS line (HIGH for data, LOW for instructions), 
# pulsing the E line, and sending the data one parallel 'nibble' at a time. 
def lcd_byte(bits, mode):

  GPIO.output(LCD_RS, mode) # RS
  print("Sending %s in mode %d" % ('{:08b}'.format(bits), mode))

  # Send high (leftmost) bits
  GPIO.output(LCD_D4, False)
  GPIO.output(LCD_D5, False)
  GPIO.output(LCD_D6, False)
  GPIO.output(LCD_D7, False)
  GPIO.output(LCD_D4, bits&0b00010000==0b000010000)
  GPIO.output(LCD_D5, bits&0b00100000==0b00100000)
  GPIO.output(LCD_D6, bits&0b01000000==0b01000000)
  GPIO.output(LCD_D7, bits&0b10000000==0b10000000)

  # Pulse "E" line
  time.sleep(E_DELAY)
  GPIO.output(LCD_E, True)
  time.sleep(E_PULSE)
  GPIO.output(LCD_E, False)
  time.sleep(E_DELAY)

  # Send low (rightmost) bits
  GPIO.output(LCD_D4, False)
  GPIO.output(LCD_D5, False)
  GPIO.output(LCD_D6, False)
  GPIO.output(LCD_D7, False)
  GPIO.output(LCD_D4, bits&0b00000001==0b00000001)
  GPIO.output(LCD_D5, bits&0b00000010==0b00000010)
  GPIO.output(LCD_D6, bits&0b00000100==0b00000100)
  GPIO.output(LCD_D7, bits&0b00001000==0b00001000)

  # Pulse "E" line
  time.sleep(E_DELAY)
  GPIO.output(LCD_E, True)
  time.sleep(E_PULSE)
  GPIO.output(LCD_E, False)
  time.sleep(E_DELAY)


def lcd_toggle_enable():
  # Toggle enable
  time.sleep(E_DELAY)
  GPIO.output(LCD_E, True)
  time.sleep(E_PULSE)
  GPIO.output(LCD_E, False)
  time.sleep(E_DELAY)

if __name__ == '__main__':

  try:
    main()
  except KeyboardInterrupt:
    pass
  finally:
    lcd_byte(0b00000001,LCD_CMD) # clear display
    lcd_byte(0b00001000, LCD_CMD) # 0000 1000 Display off - 5.2.4 in datasheet
    GPIO.cleanup()
