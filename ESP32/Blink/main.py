import machine
import time
pin = machine.Pin(2, machine.Pin.OUT)
#while True:
for i in range(10):
    pin.value(1) 
    time.sleep(1)
    pin.value(0) 
    time.sleep(1)
