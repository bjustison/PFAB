# Adafruit 16x2 Negative RGB LCD + Extras 
# Raspberry Pi 2 with Vilros cobbler and breadboard
# Adafruit Python Library https://github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code.git
# Original File Adafruit-Raspberry-Pi-Python-Code/Adafruit_CharLCD/Adafruit_CharLCD_IPclock_example.py
# Test file to change display color
# Bob Justison
# 2015-02-24

from subprocess import *
from time import sleep, strftime
from datetime import datetime
import Adafruit_CharLCD as LCD
#import Adafruit_CharLCD
#Adafruit_CharLCD = LCD

# Raspberry Pi configuration:
lcd_rs = 27  # Change this to pin 21 on older revision Raspberry Pi's
lcd_en = 22
lcd_d4 = 25
lcd_d5 = 24
lcd_d6 = 23
lcd_d7 = 18
lcd_red   = 4
lcd_green = 17
lcd_blue  = 7  # Pin 7 is CE1


# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows    = 2

# Initialize the LCD using the pins above.
lcd = LCD.Adafruit_RGBCharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7,
								lcd_columns, lcd_rows, lcd_red, lcd_green, lcd_blue)

cmd = "ip addr show wlan0 | grep inet | awk '{print $2}' | cut -d/ -f1"

# Use lcd.set_color() to change color.
# Blue  (0.0, 0.0, 1.0)
# Red   (1.0, 0.0, 0.0)
# Green (0.0, 1.0, 0.0)

def run_cmd(cmd):
    p = Popen(cmd, shell=True, stdout=PIPE)
    output = p.communicate()[0]
    return output

while 1:
    lcd.set_color(0.0, 0.0, 1.0) 
    lcd.clear()
    ipaddr = run_cmd(cmd)
    lcd.message(datetime.now().strftime('%b %d  %H:%M:%S\n'))
    lcd.message('IP %s' % (ipaddr))
    sleep(2)
