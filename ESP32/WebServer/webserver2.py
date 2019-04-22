import picoweb
import network
 
#### Parsing function
def qs_parse(qs):
 
  parameters = {}
  ampersandSplit = qs.split("&")
 
  for element in ampersandSplit:
    equalSplit = element.split("=")
    parameters[equalSplit[0]] = equalSplit[1]
 
  return parameters
 
#### WiFi Connection
ssid = "Wifi-A"
password = "789456123"
station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(ssid, password)
 
while station.isconnected() == False:
  pass
 
ip = station.ifconfig()
 
#### Picoweb app
app = picoweb.WebApp("myApp")
 
@app.route("/query")
def query(req, resp):
    queryString = req.qs
 
    parameters = qs_parse(queryString)
 
    yield from picoweb.start_response(resp)
    yield from resp.awrite("Parameter 1 value: " + parameters["param1"] + "\n")
    yield from resp.awrite("Parameter 2 value: " + parameters["param2"])
 
app.run(debug=True, host =ip[0])