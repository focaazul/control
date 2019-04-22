#*****************************************************************
#Este código habilita un servidor Web en el ESP32
# y desde la pagina de inicio se puede encender o apagar el led
# azul de la placa
# Obtenido de # Complete project details at https://RandomNerdTutorials.com
# Complete project details at https://RandomNerdTutorials.com
#
#*****************************************************************
# Estas líneas son para importar la librería que me permite crear un socket.
try:
  import usocket as socket
except:
  import socket
#********************************
from machine import Pin # Importo librería que contiene info del ESP32
import network  # Importo librería que contiene clases para manejar wifi

# https://docs.micropython.org/en/latest/library/esp.html
# Esta línea apaga los mensajes de Debug
import esp
esp.osdebug(None)
# Importo la Librería de recolección de Basura.
# Ayuda a eliminar referencias circulares de memorias.
import gc
gc.collect()
#Defino los pines de salida para manejar el LCD
"""Implements a HD44780 character LCD connected via ESP32 GPIO pins."""
import utime
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

# Defino los parámetros para conectarme a la Wifi
#ssid = 'WMKCD'
#password = '15414229'

ssid = 'WMKCD'
password = '15414229'

#Defini un objeto station que depende de la librería network.
station = network.WLAN(network.STA_IF)
#Activo el objeto starion
station.active(True)
# Le paso los parámetros de wifi para que el objeto se conecte.
station.connect(ssid, password)

# Me quedo en el bucle mientras no esté conectado a la Wifi.
while station.isconnected() == False:
	utime.sleep(15)
  pass

# Print a 1 el menasje  de conectado
lcd.set_line(0)
lcd.message("Conectado a wifi",1)
# rint('Connection successful')
# Muestro la IP para que se puedan conectat a Webserver con esa IP
print(station.ifconfig())
ip_address=tuple(station.ifconfig())
lcd.set_line(1)
texto="ip "+ip_address[0];
lcd.message( texto,1)# Defino el pin 2 como salida y llamo led al objeto.
led = Pin(2, Pin.OUT)

# Defino una función llamada web_page
def web_page():
  if led.value() == 1:
    gpio_state="ON" # Si está encedido la variable salida gpio_state tiene el texto ON
  else:
    gpio_state="OFF" # Si está apagado la variable salida gpio_state tiene el texto OFF
  #código HtML de la página.
  html = """<html>
		<head> 
			<title>ESP32 Web Server. versión 1.0</title> 
			<meta name="viewport" content="width=device-width, initial-scale=1">
  			<link rel="icon" href="data:,"> 
			<style>
				html{font-family: Helvetica; display:inline-block; margin: 0px auto; text-align: center;}
	  			h1{color: #0F3376; padding: 2vh;}
				p{font-size: 1.5rem;}.button{display: inline-block; background-color: #e7bd3b; border: none; 
	  			border-radius: 4px; color: white; padding: 16px 40px; text-decoration: none; font-size: 30px; margin: 2px; cursor: pointer;}
	  			.button2{background-color: #4286f4;}
			</style>
		</head>
		<body> 
			<h1>ESP32 Web Server Versión 1.0 </h1> 
			  <p>Estado de Salida GPIO: <strong>""" + gpio_state + """</strong></p>
			<p><a href="/?led=on"><button class="button">ON</button></a></p>
  			<p><a href="/?led=off"><button class="button button2">OFF</button></a></p>
		</body>
	</html>""" #Fin de comentario multilinea.
  return html
# https://docs.micropython.org/en/latest/library/usocket.html
# creo un Socket llamado s 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Enlazo el socket a la dirección ip que sea, puerto 80
s.bind(('', 80))
# 5 , número de conexiones no aceptadas antes de ser rechazadas.
s.listen(5)

while True:
# Acepto la conexión
  conn, addr = s.accept()
# s.accept() retorna 2 valores, un objeto conn de la conexión y la ip 
# addr que tiene la IP de Origen que solicita el Servicio Web.
  print('Got a connection from %s' % str(addr))
  request = conn.recv(1024)
  request = str(request)
  print('Content = %s' % request)
  led_on = request.find('/?led=on')
  led_off = request.find('/?led=off')
  if led_on == 6:
    print('LED ON')
    led.value(1)
  if led_off == 6:
    print('LED OFF')
    led.value(0)
  response = web_page()
  conn.send(response)
  conn.close()








 


