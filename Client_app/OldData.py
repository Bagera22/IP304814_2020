from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import *
import tkinter.font as font
import numpy as np
import serial as sr
import csv

skipfirst = True


root = Tk()
root.title("Welcome to Brage test")

verdi = Entry(root, width=50)
verdi.grid(row=0, column=2)

def on_open():
    temp = []
    Wind = []
    Praser = []
    roll = []
    hading = []
    pitch = []
    Latitude = []
    Longitude = []
    global skipfirst
    print("1")
    with open(verdi.get()+".csv") as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            if not skipfirst:
                temp.append(float(row[5]))
                if "0-" in row[6]:
                    row[6] = row[6].replace("0-", "")
                if not "" == row[9]:
                    row[9] = row[9].replace("N", "")
                    Latitude.append(float(row[9]))
                if not "" == row[10]:
                    row[10] = row[10].replace("E", "")
                    Longitude.append(float(row[10]))
                Wind.append(float(row[6]))
                Praser.append(float(row[4]))
                roll.append(float(row[1]))
                hading.append(float(row[3]))
                pitch.append(float(row[2]))
            skipfirst = False
        print("1")
            
        fig1 = Figure()
        fig2 = Figure()
        fig3 = Figure()
        fig4 = Figure()
        fig5 = Figure()
        fig6 = Figure()
        fig7 = Figure()
        fig8 = Figure()
        tg = fig1.add_subplot(111)
        vg = fig2.add_subplot(111)
        pg = fig3.add_subplot(111)
        rg = fig4.add_subplot(111)
        hg = fig5.add_subplot(111)
        pig = fig6.add_subplot(111)
        Lati = fig7.add_subplot(111)
        Long = fig8.add_subplot(111)
        print(temp)

        tg.set_title('Temp')
        tg.set_xlabel('Sample')
        tg.set_ylabel('C')
        tg.set_xlim(0,(len(temp)))
        tg.set_ylim(-15,40)
        tg_height = (3,2)
        lines = tg.plot(np.arange(len(temp)),temp)[0]
        

        vg.set_title('Wind')
        vg.set_xlabel('Sample')
        vg.set_ylabel('m/s')
        vg.set_xlim(0,len(Wind)-1)
        vg.set_ylim(-2,30)
        lines2 = vg.plot(np.arange(0,len(Wind)),Wind)[0]

        pg.set_title('Pressure')
        pg.set_xlabel('Sample')
        pg.set_ylabel('Pa')
        pg.set_xlim(0,len(Praser)-1)
        pg.set_ylim(500,1200)
        lines3 = pg.plot(np.arange(0,len(Praser)),Praser)[0]

        rg.set_title('Roll')
        rg.set_xlabel('Sample')
        rg.set_ylabel('Deg')
        rg.set_xlim(0,len(roll)-1)
        rg.set_ylim(-180,180)
        lines4 = rg.plot(np.arange(0,len(roll)),roll)[0]

        hg.set_title('Heading')
        hg.set_xlabel('Sample')
        hg.set_ylabel('Deg')
        hg.set_xlim(0,len(roll)-1)
        hg.set_ylim(0,360)
        lines5 = hg.plot(np.arange(0,len(hading)),hading)[0]

        pig.set_title('Pitch')
        pig.set_xlabel('Sample')
        pig.set_ylabel('Deg')
        pig.set_xlim(0,len(roll)-1)
        pig.set_ylim(-180,180)
        lines6 = pig.plot(np.arange(0,len(pitch)),pitch)[0]

        Lati.set_title('Latitude')
        Lati.set_xlabel('Sample')
        Lati.set_ylabel('N')
        Lati.set_xlim(0,len(Latitude)-1)
        Lati.set_ylim(6200,6300)
        lines7 = Lati.plot(np.arange(0,len(Latitude)),Latitude)[0]
        print(Latitude)

        Long.set_title('Longitude')
        Long.set_xlabel('Sample')
        Long.set_ylabel('E')
        Long.set_xlim(0,len(Longitude)-1)
        Long.set_ylim(600,700)
        lines8 = Long.plot(np.arange(0,len(Longitude)),Longitude)[0]

        canvas = FigureCanvasTkAgg(fig1, master=root)
        canvas.get_tk_widget().grid(row=1, column=1)
        canvas2 = FigureCanvasTkAgg(fig2, master=root)
        canvas2.get_tk_widget().grid(row=2, column=1)
        canvas3 = FigureCanvasTkAgg(fig3, master=root)
        canvas3.get_tk_widget().grid(row=1, column=2)
        canvas4 = FigureCanvasTkAgg(fig4, master=root)
        canvas4.get_tk_widget().grid(row=2, column=2)
        canvas5 = FigureCanvasTkAgg(fig5, master=root)
        canvas5.get_tk_widget().grid(row=1, column=3)
        canvas6 = FigureCanvasTkAgg(fig6, master=root)
        canvas6.get_tk_widget().grid(row=2, column=3)
        canvas7 = FigureCanvasTkAgg(fig7, master=root)
        canvas7.get_tk_widget().grid(row=1, column=4)
        canvas8 = FigureCanvasTkAgg(fig8, master=root)
        canvas8.get_tk_widget().grid(row=2, column=4)
        

        canvas.draw()
        skipfirst = True

def on_open_time():
    temp = []
    Wind = []
    Praser = []
    roll = []
    hading = []
    pitch = []
    Latitude = []
    Longitude = []
    timestamp = verdi.get().split(",")

    teg = False
    print("1")
    with open(timestamp[0]+".csv") as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            if teg or timestamp[1] == row[8]:
                if not timestamp[2] == row[8]:
                    temp.append(float(row[5]))
                    if "0-" in row[6]:
                        row[6] = row[6].replace("0-", "")

                    if not "" == row[9]:
                        row[9] = row[9].replace("N", "")
                        Latitude.append(float(row[9]))
                    if not "" == row[10]:
                        row[10] = row[10].replace("E", "")
                        Longitude.append(float(row[10]))
                    Wind.append(float(row[6]))
                    Praser.append(float(row[4]))
                    roll.append(float(row[1]))
                    hading.append(float(row[3]))
                    pitch.append(float(row[2]))
                teg = True
            
        print("1")
            
        fig1 = Figure()
        fig2 = Figure()
        fig3 = Figure()
        fig4 = Figure()
        fig5 = Figure()
        fig6 = Figure()
        fig7 = Figure()
        fig8 = Figure()
        tg = fig1.add_subplot(111)
        vg = fig2.add_subplot(111)
        pg = fig3.add_subplot(111)
        rg = fig4.add_subplot(111)
        hg = fig5.add_subplot(111)
        pig = fig6.add_subplot(111)
        Lati = fig7.add_subplot(111)
        Long = fig8.add_subplot(111)
        print(temp)

        tg.set_title('Temp')
        tg.set_xlabel('Sample')
        tg.set_ylabel('C')
        tg.set_xlim(0,(len(temp)))
        tg.set_ylim(-15,40)
        tg_height = (3,2)
        lines = tg.plot(np.arange(len(temp)),temp)[0]
        

        vg.set_title('Wind')
        vg.set_xlabel('Sample')
        vg.set_ylabel('m/s')
        vg.set_xlim(0,len(Wind)-1)
        vg.set_ylim(-2,30)
        lines2 = vg.plot(np.arange(0,len(Wind)),Wind)[0]

        pg.set_title('Pressure')
        pg.set_xlabel('Sample')
        pg.set_ylabel('Pa')
        pg.set_xlim(0,len(Praser)-1)
        pg.set_ylim(500,1200)
        lines3 = pg.plot(np.arange(0,len(Praser)),Praser)[0]

        rg.set_title('Roll')
        rg.set_xlabel('Sample')
        rg.set_ylabel('Deg')
        rg.set_xlim(0,len(roll)-1)
        rg.set_ylim(-180,180)
        lines4 = rg.plot(np.arange(0,len(roll)),roll)[0]

        hg.set_title('Heading')
        hg.set_xlabel('Sample')
        hg.set_ylabel('Deg')
        hg.set_xlim(0,len(roll)-1)
        hg.set_ylim(0,360)
        lines5 = hg.plot(np.arange(0,len(hading)),hading)[0]

        pig.set_title('Pitch')
        pig.set_xlabel('Sample')
        pig.set_ylabel('Deg')
        pig.set_xlim(0,len(roll)-1)
        pig.set_ylim(-180,180)
        lines6 = pig.plot(np.arange(0,len(pitch)),pitch)[0]

        Lati.set_title('Latitude')
        Lati.set_xlabel('Sample')
        Lati.set_ylabel('N')
        Lati.set_xlim(0,len(Latitude)-1)
        Lati.set_ylim(6200,6300)
        lines7 = Lati.plot(np.arange(0,len(Latitude)),Latitude)[0]
        
        Long.set_title('Longitude')
        Long.set_xlabel('Sample')
        Long.set_ylabel('E')
        Long.set_xlim(0,len(Longitude)-1)
        Long.set_ylim(600,700)
        lines8 = Long.plot(np.arange(0,len(Longitude)),Longitude)[0]

        canvas = FigureCanvasTkAgg(fig1, master=root)
        canvas.get_tk_widget().grid(row=1, column=1)
        canvas2 = FigureCanvasTkAgg(fig2, master=root)
        canvas2.get_tk_widget().grid(row=2, column=1)
        canvas3 = FigureCanvasTkAgg(fig3, master=root)
        canvas3.get_tk_widget().grid(row=1, column=2)
        canvas4 = FigureCanvasTkAgg(fig4, master=root)
        canvas4.get_tk_widget().grid(row=2, column=2)
        canvas5 = FigureCanvasTkAgg(fig5, master=root)
        canvas5.get_tk_widget().grid(row=1, column=3)
        canvas6 = FigureCanvasTkAgg(fig6, master=root)
        canvas6.get_tk_widget().grid(row=2, column=3)
        canvas7 = FigureCanvasTkAgg(fig7, master=root)
        canvas7.get_tk_widget().grid(row=1, column=4)
        canvas8 = FigureCanvasTkAgg(fig8, master=root)
        canvas8.get_tk_widget().grid(row=2, column=4)
        

        canvas.draw()
        skipfirst = True
OpenFil = Button(root, text="Open", command=on_open)
OpenFil.grid(row=0, column=0)

OpenFilt = Button(root, text="Time start", command=on_open_time)
OpenFilt.grid(row=0, column=1)


root.mainloop()