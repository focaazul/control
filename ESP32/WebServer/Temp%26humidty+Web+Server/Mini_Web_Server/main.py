###############################################################################
# Temp&humidty Web Server
#
# Created by Zerynth Team 2018 CC
# Authors: K.Hamdy
###############################################################################

# import streams & socket
import streams
import socket

# import the wifi interface
from wireless import wifi
from espressif.esp32net import esp32wifi as wifi_driver #importing Esp32 Wifi driver
from stm.hts221 import hts221

streams.serial() #initate serial driver
temp_hum = hts221.HTS221( I2C0,D16) #initiate i2C protocol with the sensor


WifiAP_name = "TOI"
Wifi_Pass = "!FH565sjkwork!"

wifi_driver.auto_init()
print("Establishing Link...")
try:
    wifi.link(WifiAP_name,wifi.WIFI_WPA2,Wifi_Pass)
except Exception as e:
    print("ooops, something wrong while linking :(", e)
    while True:
        sleep(1000)

print("Linked!")

# Let's print our ip, it will be needed soon
info = wifi.link_info()
print("My IP is:",info[0])
print("please open this IP in your browser to view the webpage")

# Now let's create a socket and listen for incoming connections on port 80
sock = socket.socket()
sock.bind(80)
sock.listen()


while True:
    try:
        # Type in your browser the board ip!
        print("Waiting for connection...")
        # here we wait for a connection
        clientsock,addr = sock.accept()
        print("Incoming connection from",addr)
        
        # yes! a connection is ready to use
        # first let's create a SocketStream
        # it's like a serial stream, but with a socket underneath.
        # This way we can read and print to the socket
        client = streams.SocketStream(clientsock)
        temp, hum = temp_hum.get_temp_humidity()
        # let's read all the HTTP headers from the browser
        # stop when a blank line is received
        line = client.readline()
        while line!="\n" and line!="\r\n":
            line = client.readline()
        print("HTTP request received!")
        
        # let's now send our headers (very minimal)
        # hint: \n is added by print
        print("HTTP/1.1 200 OK\r",stream=client)
        print("Content-Type: text/html\r",stream=client)
        print("Connection: close\r\n\r",stream=client)
        print("<head><title>Esp32 Temperature and humidity web server using Zerynth IDE</title></head>",stream=client)
        print("<body><h1 style=\"text-align:center;color:#9B3A25\">Esp32 Temperature and humidity web server using Zerynth IDE</h1><p>This is Temperature and humidity web server using Esp32 and Hts221 Temp&humd sensor</p><hr>",stream=client)
        print("<h2 style = \"color:#9B3A25\">Current temperature and humidity</h2><p>Temp : ",temp," celsius, ",stream=client)
        print("Humidty : ",hum," %</p><hr>",stream=client)
        print("<h2 style = \"color:#9B3A25\">Links</h2><p>Zerynth IDE: <a href=\"https://www.zerynth.com\">www.zerynth.com</a></p>",stream=client)
        print("<p>What is Zerynth: <a href=\"https://www.zerynth.com/get-started/#what-is-zerynth\">What is Zerynth?</a></p>",stream=client)
        print("<p>Getting Started: <a href=\"https://docs.zerynth.com/latest/official/core.zerynth.docs/gettingstarted/docs/index.html\">Click Here</a></p>",stream=client)
        print("</body></html>",stream=client)

        # close connection and go waiting for another one
        client.close()
    except Exception as e:
        print("ooops, something wrong:",e)
        

