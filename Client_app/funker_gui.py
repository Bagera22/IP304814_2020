import paho.mqtt.client as mqtt
from tkinter import *
import tkinter.font as font


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("box/#")

# The callback for when a PUBLISH message is received from the server.
def on_message_heading(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    heading.configure(text=str("Heading: " + msg.payload.decode("utf-8") + "N  "), font=myFont)

def on_message_roll(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    roll.configure(text=str("Roll: " + msg.payload.decode("utf-8") + "Deg  "), font=myFont)

def on_message_pitch(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    pitch.configure(text=str("Pitch: " + msg.payload.decode("utf-8") + "Deg  "), font=myFont)

def on_message_temp(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    temp.configure(text=str("Temp: " + msg.payload.decode("utf-8") + "C  "), font=myFont)

def on_message_gps(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    dataPacket=str(msg.payload.decode("utf-8"))
    gps.configure(text="GPS: " + dataPacket, font=myFont)

def on_message_vind(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    vind.configure(text=str("Vind: " + msg.payload.decode("utf-8") + "m/s  "), font=myFont)

def on_message_trykk(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    trykk.configure(text=str("Pressure: " + msg.payload.decode("utf-8") + "Pa  "), font=myFont)

client = mqtt.Client()
client.on_connect = on_connect
client.message_callback_add('box/heading', on_message_heading)
client.message_callback_add('box/roll', on_message_roll)
client.message_callback_add('box/pitch', on_message_pitch)
client.message_callback_add('box/temp', on_message_temp)
client.message_callback_add('box/gps', on_message_gps)
client.message_callback_add('box/vind', on_message_vind)
client.message_callback_add('box/trykk', on_message_trykk)
# client.on_message = on_message
client.connect("mqtt.eclipse.org", 1883, 60)
client.loop_start()

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.



window = Tk()
myFont = font.Font(family='Helvetica', size=20, weight='bold')
window.geometry('700x200')
window.title("Welcome to Brage app")
heading = Label(window, text=("Heading: " + "111" + " N  "), font=myFont)
heading.grid(row=0, column=0)
roll = Label(window, text=("Roll: " + "111" + " Deg  "), font=myFont)
roll.grid(row=1, column=0)
pitch = Label(window, text=("Pitch: " + "111" + " Deg  "), font=myFont)
pitch.grid(row=2, column=0)
temp = Label(window, text=("Temp: " + "111" + " C  "), font=myFont)
temp.grid(row=0, column=1)
gps = Label(window, text=("GPS: " + "111" + " N  "), font=myFont)
gps.grid(row=1, column=1)
vind = Label(window, text=("Vind: " + "111" + " m/s  "), font=myFont)
vind.grid(row=2, column=1)
trykk = Label(window, text=("Pressure: " + "111" + " Pa  "), font=myFont)
trykk.grid(row=3, column=1)

window.mainloop()
