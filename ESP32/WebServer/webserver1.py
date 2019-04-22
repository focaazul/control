
#http://dfrobot.blogspot.com/2017/10/esp32-micropython-tutorial-http.html

import network
#def connect():
ssid = "Wifi-A"
password = "789456123"
station = network.WLAN(network.STA_IF)
if station.isconnected() == True:
    print("Already connected")
#return
station.active(True)
station.connect(ssid, password)
while station.isconnected() == False:
    pass
    print("Connection successful")
    print(station.ifconfig())

import upip
#upip.install('micropython-uasyncio')
#upip.install('micropython-pkg_resources')

import os
#os.listdir()

import uasyncio
import pkg_resources
#os.mkdir("picoweb")
#os.listdir()

import picoweb
app = picoweb.WebApp(none)
@app.route("/")
def index(req, resp):
    yield from picoweb.start_response(resp)
    yield from resp.awrite("Hello world from picoweb running on the ESP32")
    app.run(debug=True, host = "192.168.1.67")
   