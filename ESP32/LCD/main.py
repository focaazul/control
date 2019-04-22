"""Implements a HD44780 character LCD connected via ESP32 GPIO pins."""
from LCD import  CharLCD
from machine import Pin
import machine
rs_pin= machine.Pin(22, machine.Pin.OUT)
enable= machine.Pin(23, machine.Pin.OUT)
d4_pin= machine.Pin(5, machine.Pin.OUT)
d5_pin= machine.Pin(18, machine.Pin.OUT)
d6_pin= machine.Pin(19, machine.Pin.OUT)
d7_pin= machine.Pin(21, machine.Pin.OUT)

lcd = CharLCD(rs=22, en=23, d4=5, d5=18, d6=19, d7=21,
                  cols=16, rows=2)

    # Print a 2 line centered message
lcd.message('Hola', 2)
lcd.set_line(1)
lcd.message('German!', 2)



