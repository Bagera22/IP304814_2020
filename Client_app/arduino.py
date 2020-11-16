import paho.mqtt.client as mqtt
from time import *
import serial

ad=serial.Serial('com5',115200)
sleep(1)


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("box/#")


client = mqtt.Client()
client.on_connect = on_connect
client.connect("mqtt.eclipse.org", 1883, 60)
client.loop_start()

while (True):
    while (ad.inWaiting()==0):
        pass
    
    dataPacket=ad.readline()
    dataPacket=str(dataPacket,'utf-8')
    splitPacket=dataPacket.split(",")

    client.publish("box/heading", (splitPacket[2]))
    client.publish("box/roll", (splitPacket[0]))
    client.publish("box/pitch", (splitPacket[1]))
    client.publish("box/temp", (splitPacket[3]))
    client.publish("box/gps", (splitPacket[4]))
    client.publish("box/vind", (splitPacket[5]))
    client.publish("box/3D", (splitPacket[0] + "," + splitPacket[1]+ "," + splitPacket[2]))

