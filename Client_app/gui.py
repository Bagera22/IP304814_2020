#-------------------------------------------------------------------------------
# Name:        module3
# Purpose:
#
# Author:      Brage
#
# Created:     08.11.2020
# Copyright:   (c) Brage 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from tkinter import *
import tkinter.font as font
from PIL import ImageTk,Image
import paho.mqtt.client as mqtt
import threading

root = Tk()
hading = "1"
roll = "1"
pitch = "1"
temp = "1"
gps = "1"

def on_message_hading(mosq, obj, msg):
    hading = str(msg.payload)
    print(hading)
    myHading = Label(root, text=str("Hading: " + hading + "N  "), font=myFont)
    myHading.grid(row=0 , column=0)



def on_message_pitch(mosq, obj, msg):
    pitch = str(msg.payload)
    print(pitch)
    myPitch = Label(root, text=str("Pitch: " + pitch + "deg  "), font=myFont)
    myPitch.grid(row=2 , column=0)

def on_message_roll(mosq, obj, msg):
    roll = str(msg.payload)
    print(roll)
    myRoll = Label(root, text=str("Roll: " + roll + "deg  "), font=myFont)
    myRoll.grid(row=1 , column=0)

def on_message_temp(mosq, obj, msg):
    temp = str(msg.payload)
    myTemp = Label(root, text=str("Temp: " + temp + "C"), font=myFont)
    myTemp.grid(row=0 , column=1)

def on_message_gps(mosq, obj, msg):
    gps = str(msg.payload)
    myGps = Label(root, text=str("GPS: " + gps + "N"), font=myFont)
    myGps.grid(row=1 , column=1)

def on_message(mosq, obj, msg):
    print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))


myFont = font.Font(family='Helvetica', size=20, weight='bold')
mqttc = mqtt.Client()

mqttc.message_callback_add('box/heding', on_message_hading)
mqttc.message_callback_add('box/roll', on_message_roll)
mqttc.message_callback_add('box/pitch', on_message_pitch)
mqttc.message_callback_add('box/temp', on_message_temp)
mqttc.message_callback_add('box/gps', on_message_gps)
mqttc.on_message = on_message
mqttc.connect("mqtt.eclipse.org", 1883, 60)
mqttc.subscribe("box/#")
mqttc.loop_forever()



