i###############################################################################
# Se prende y se apaga el Led desde una página Web servida
#por el ESPN32
#
# Created by Daniel Refosco
###############################################################################
# En ESP32S v1.1 el pin 2 esta conectado a un led

import machine #para manejar los pines
pin = machine.Pin(2, machine.Pin.OUT) #Defino el pin 2 como Salida
import picoweb # para Servidor Web
import network #para conectarma a Wifi
import time


nombressid = Wifi-A  #Nombre de la Wlan
password = 789456123 #Password de la Wlan.

connect-wifi(nombressid,password)

ip=sta_if.ifconfig()[0]
print("La ip del Servidor Web es: ".format(ip))
app = picoweb.WebApp(__name__)
index_html = " " "
<html>
  <body>
    <h1> LED On/ Off</h1>
    <h3> Esta pagina prende o apaga el led del ESP32</h3>
    <p><a href="/led-on">Encender </a></p>
    <p><a href="/led-off">Apagar </a></p>
  </body>
</html>
" " "

@app.route('/led-on')
    
#Función que enciende el Led
def led-on():
    pin.value(1) #Prendo led
@app.route('/led-off')
#Función que enciende el Led
def led-off():
 pin.value(0) #Apago led

    


#Función que conecta a Wifi, en caso de conectarse, el led parpadea 5 veces.
def connect-wifi(nombressid, password):
    wifi = network.WLAN(network.STA_IF); 
    wifi.active(True)
    wifi.connect(nombressid, password) # Connect to an AP
#Bucle infinito que parpadea led si está conectado a Wifi
    while  i < 10:  #intenta conectarse hasta 10 veces.
    
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
                i=i+1
            
