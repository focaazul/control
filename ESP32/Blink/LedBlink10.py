###############################################################################
# Led Blink
#
# Created by Daniel Refosco
###############################################################################
# En ESP32S v1.1 el pin 2 esta conectado a un led

import machine
import time
pin = machine.Pin(2, machine.Pin.OUT)
for i in range (10):
    pin.value(1) #Prendo led
    time.sleep(1)
    pin.value(0) #Apago led
    time.sleep(1)
