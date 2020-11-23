import serial
import paho.mqtt.client as mqtt
import pandas as pd

client = mqtt.Client()
client.connect("mqtt.eclipse.org", 1883, 60)  # connecting to a MQTT client

ser = serial.Serial('COM5', baudrate=115200)  # connecting to serial port COM5
x = 0
y = 1

#  For making a csv file locally
fields = ['Roll', 'Pitch', 'Heading', 'Pressure(Pha)', 'Temperature', 'WindSpeed', 'Date', 'Time', 'latitude',
          'longitude', 'Altitude']
logList = []  # List to hold all incoming data
#  List for testing and making a csv file locally
rollList = []  # List to hold roll data
pitchList = []  # List to hold pitch data
headingList = []  # List to hold heading data
pressureList = []  # List to hold pressure data
temperatureList = []  # List to hold temperature data
windSpeedList = []  # List to hold wind speed data
dateList = []  # List to hold date's
timeList = []  # List to hold  time
latitudeList = []  # List to hold latitude data
longitudeList = []  # List to hold longitude data
altitudeList = []  # List to hold altitude data


#  test function to print all incoming data
def printall():
    print(logList[0])
    print(logList[1])
    print(logList[2])
    print(logList[3])
    print(logList[4])
    print(logList[5])
    if len(logList) >= 10:
        print(logList[6])
        print(logList[7])
        print(logList[8])
        print(logList[9])
        print(logList[10])


while (1):  # An endless while loop

    serialString = ser.readline()  # read on line from the serial monitor

    string = serialString.decode('Ascii')  # Decode into string

    # Making a list to hold the incoming data read from the serial monitor
    logList = string.split(",")

    #  publishing to a MQTT client
    client.publish("box/roll", (logList[0]))
    client.publish("box/pitch", (logList[1]))
    client.publish("box/heading", (logList[2]))
    client.publish("box/trykk", (logList[3]))
    client.publish("box/temp", (logList[4]))
    client.publish("box/vind", (logList[5]))
    print(logList[5])  # make sure it only publish when when it has the GPS da available
    if len(logList) >= 10:
        client.publish("box/dato", logList[6])
        client.publish("box/tid", logList[7])
        client.publish("box/gps", (logList[8] + "," + logList[9]))
        client.publish("box/altitude", logList[10])
    client.publish("box/3D", (logList[0] + "," + logList[1] + "," + logList[2]))

    #  appending each sensor data into its own list
    rollList.append(logList[0])
    pitchList.append(logList[1])
    headingList.append(logList[2])
    pressureList.append(logList[3])
    temperatureList.append(logList[4])
    windSpeedList.append(logList[5])
    if len(logList) >= 10:
        dateList.append(logList[6])
        timeList.append(logList[7])
        latitudeList.append(logList[8])
        longitudeList.append(logList[9])
        if len(logList[10]):
            altitudeList.append(logList[10])
        else:
            altitudeList.append(logList[10].replace("\r\n", ""))
    else:  # appends a blank string
        dateList.append("")
        timeList.append("")
        latitudeList.append("")
        longitudeList.append("")
        altitudeList.append("")

    # making a dictionary for all the list with sensor data
    dict = {'Roll': rollList, 'Pitch': pitchList, 'Heading': headingList, 'Pressure(Pha)': pressureList,
            'Temperature': temperatureList,
            'WindSpeed': windSpeedList, 'Date': dateList, 'Time': timeList, 'latitude': latitudeList,
            'longitude': longitudeList, 'Altitude': altitudeList}
    # opening the csv file in 'w' mode
    df = pd.DataFrame(dict)

    # saving the csv file
    df.to_csv('Datalog.csv')
