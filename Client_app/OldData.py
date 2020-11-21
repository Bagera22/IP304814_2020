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
verdi.grid(row=0, column=1)

def on_open():
    temp = []
    Wind = []
    Praser = []
    roll = []
    global skipfirst
    print("1")
    with open(verdi.get()+".csv") as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            if not skipfirst:
                temp.append(float(row[5]))
                Wind.append(float(row[6]))
                Praser.append(float(row[4]))
                roll.append(float(row[1]))
            skipfirst = False
        print("1")
            
        fig1 = Figure()
        fig2 = Figure()
        fig3 = Figure()
        fig4 = Figure()
        tg = fig1.add_subplot(111)
        vg = fig2.add_subplot(111)
        pg = fig3.add_subplot(111)
        rg = fig4.add_subplot(111)
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

        canvas = FigureCanvasTkAgg(fig1, master=root)
        canvas.get_tk_widget().grid(row=1, column=1)
        canvas2 = FigureCanvasTkAgg(fig2, master=root)
        canvas2.get_tk_widget().grid(row=2, column=1)
        canvas3 = FigureCanvasTkAgg(fig3, master=root)
        canvas3.get_tk_widget().grid(row=1, column=2)
        canvas4 = FigureCanvasTkAgg(fig4, master=root)
        canvas4.get_tk_widget().grid(row=2, column=2)
        

        canvas.draw()
        skipfirst = True

OpenFil = Button(root, text="Open", command=on_open)
OpenFil.grid(row=0, column=0)


root.mainloop()