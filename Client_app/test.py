import paho.mqtt.client as mqtt
from tkinter import *
import tkinter.font as font

root = Tk()
root.title("Welcome to Brage test")

verdi = Entry(root, width=50)
verdi.pack()

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("box/#")

def setHeading():
    client.publish("box/heading", verdi.get())

def setRoll():
    client.publish("box/roll", verdi.get())

def setPitch():
    client.publish("box/pitch", verdi.get())

def setTemp():
    client.publish("box/temp", verdi.get())

def setWind():
    client.publish("box/vind", verdi.get())

def set3D():
    client.publish("box/3D", verdi.get() + " , 123 , 132")


client = mqtt.Client()
client.on_connect = on_connect
client.connect("mqtt.eclipse.org", 1883, 60)
client.loop_start()


heading = Button(root, text="heading", command=setHeading)
heading.pack()

roll = Button(root, text="roll", command=setRoll)
roll.pack()

pitch = Button(root, text="pitch", command=setPitch)
pitch.pack()

temp = Button(root, text="temp", command=setTemp)
temp.pack()

S3D = Button(root, text="3D", command=set3D)
S3D.pack()

wind = Button(root, text="wind", command=setWind)
wind.pack()

root.mainloop()
