import pandas as pd
import paho.mqtt.client as mqtt
from tkinter import *
import tkinter.font as font

roll = ""
pitc = ""
heading = ""
pressure = ""
temp = ""
wind = ""
date =""
time = ""
latitude = ""
longitude = ""
altitude = ""
dataon = False
send = False
lagring = False

rollList = []
pitchList = []
headingList = []
pressureList = []
temperatureList = []
windSpeedList = []
dateList = []
timeList = []
latitudeList = []
longitudeList = []
altitudeList = []

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("box/#")

def on_message_roll(client, userdata, msg):
    global roll
   # print(msg.topic+" "+str(msg.payload))
    roll = msg.payload.decode("utf-8")
    

def on_message_heading(client, userdata, msg):
    global heading
   # print(msg.topic+" "+str(msg.payload))
    heading = msg.payload.decode("utf-8")

def on_message_pitch(client, userdata, msg):
    global pitc
    #print(msg.topic+" "+str(msg.payload))
    pitc = msg.payload.decode("utf-8")

def on_message_trykk(client, userdata, msg):
    global pressure
    #print(msg.topic+" "+str(msg.payload))
    pressure = msg.payload.decode("utf-8")

def on_message_temp(client, userdata, msg):
    global temp
   # print(msg.topic+" "+str(msg.payload))
    temp = msg.payload.decode("utf-8")

def on_message_gps(client, userdata, msg):
    global latitude
    global longitude
 #   print(msg.topic+" "+str(msg.payload))
    dataPacket = msg.payload.decode("utf-8")
    splitPacket=dataPacket.split(",")
    latitude = splitPacket[0]
    longitude = splitPacket[1]

def on_message_vind(client, userdata, msg):
    global wind
    global send
 #   print(msg.topic+" "+str(msg.payload))
    wind = str(msg.payload.decode("utf-8"))
    if "\r\n" in wind:
        wind = wind.replace("\r\n", "")
    send = True

def on_message_tid(client, userdata, msg):
    global time
    global dataon
   # print(msg.topic+" "+str(msg.payload))
    time = msg.payload.decode("utf-8")
    dataon = True

def on_message_dato(client, userdata, msg):
    global date
    #print(msg.topic+" "+str(msg.payload))
    date = msg.payload.decode("utf-8")

def on_message_altitude(client, userdata, msg):
    global altitude
    #print(msg.topic+" "+str(msg.payload))
    altitudeList = msg.payload.decode("utf-8")

def setStart():
    global lagring
    lagring = True

def setStop():
    global lagring
    lagring = False

def fil():
    global roll
    global pitc
    global heading
    global pressure
    global temp
    global wind
    global date
    global time
    global latitude
    global longitude
    global altitude
    global dataon
    global send
    global lagring

    global rollList
    global pitchList
    global headingList
    global pressureList
    global temperatureList
    global windSpeedList
    global dateList
    global timeList
    global latitudeList
    global longitudeList
    global altitudeList

    print(lagring)
    if lagring:
        
        
        if send:
            send = False
            print("heiheiheiheihehiheiheihei")
            rollList.append(roll)
            pitchList.append(pitc)
            headingList.append(heading)
            pressureList.append(pressure)
            temperatureList.append(temp)
            windSpeedList.append(wind)
            if dataon:
                dataon = False
                dateList.append(date)
                timeList.append(time)
                latitudeList.append(latitude)
                longitudeList.append(longitude)
                if "\r\n" in altitude:
                    altitudeList.append(altitude.replace("\r\n", ""))

                else:
                    altitudeList.append(altitude)


            else:
                dateList.append("")
                timeList.append("")
                latitudeList.append("")
                longitudeList.append("")
                altitudeList.append("")

        dict = {'Roll': rollList, 'Pitch': pitchList, 'Heading': headingList, 'Pressure(Pha)': pressureList, 'Temperature': temperatureList,
                'WindSpeed': windSpeedList, 'Date': dateList, 'Time': timeList, 'latitude': latitudeList, 'longitude': longitudeList, 'Altitude': altitudeList}
        #opening the csv file in 'w' mode
        datacsv = pd.DataFrame(dict)

        # saving the dataframe
        datacsv.to_csv('Datalog2.csv')
    window.after(1,fil)

fields = ['Roll', 'Pitch', 'Heading', 'Pressure(Pha)', 'Temperature', 'WindSpeed', 'Date', 'Time', 'latitude',
              'longitude', 'Altitude']



client = mqtt.Client()
client.on_connect = on_connect
client.message_callback_add('box/heading', on_message_heading)
client.message_callback_add('box/roll', on_message_roll)
client.message_callback_add('box/pitch', on_message_pitch)
client.message_callback_add('box/temp', on_message_temp)
client.message_callback_add('box/gps', on_message_gps)
client.message_callback_add('box/vind', on_message_vind)
client.message_callback_add('box/trykk', on_message_trykk)
client.message_callback_add('box/tid', on_message_tid)
client.message_callback_add('box/dato', on_message_dato)
client.message_callback_add('box/altitude', on_message_altitude)
# client.on_message = on_message
client.connect("mqtt.eclipse.org", 1883, 60)
client.loop_start()
window = Tk()
window.title("Welcome to log")

heading = Button(window, text="start", command=setStart)
heading.pack()
heading = Button(window, text="stop", command=setStop)
heading.pack()

window.after(1,fil)

window.mainloop()
