###############################################################################
# Conexión a Wifi.
# Este código hace parpadear el led azul mientras esté conectado
# a la wifi. Si se desconecta el led se apaga.
# Daniel Refosco
###############################################################################
# En ESP32S v1.1 el pin 2 esta conectado a un led

import machine 
import time # usada para time.sleep
import utime #Libreria para medir intervalos de tiempo usado para utime.sleep
import network
pin = machine.Pin(2, machine.Pin.OUT)
#http://docs.micropython.org/en/latest/library/network.WLAN.html
wifi = network.WLAN(network.STA_IF); 
wifi.active(True)
wifi.connect("localhost", "focaazul") # Connect to an AP
#Bucle infinito que parpadea led si está conectado a Wifi
while  True:
    
    if wifi.isconnected():# Check for successful connection
        # si se conecta el led parpadea 10 veces.
            pin.value(1) #Prendo led
            time.sleep(1)
            pin.value(0) #Apago led
            time.sleep(1)

    else:
        #si no se conecta el led apagado
            pin.value(0) #Apago led
            wifi.connect("localhost", "focaazul")# trato de conectarme
            print("Esperando conectar...")
            while not wifi.isconnected(): #¿No estoy conectado a la wifi?
                utime.sleep(1) #duerme por 1 segundo
