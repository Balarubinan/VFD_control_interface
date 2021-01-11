from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QPointF,QTimer
from PyQt5.QtGui import QLinearGradient, QColor, QGradient
from PyQt5.QtWidgets import QMainWindow,QDialog,QApplication
import sys
import matplotlib
matplotlib.use('Qt5Agg')
import pyqtgraph as pg
import numpy as np
import matplotlib.pyplot as plt
from random import randint,choice
import time
from threading import Thread

seconds,values_to_show,wait_time,treshold=0,0,0,0

class Graph_demo(pg.PlotWidget,QDialog):
    # Qdialogs are embedable in QWindows As QWidgets!!
    def __init__(self,*args,useColor="G"):
        super(Graph_demo, self).__init__(*args)
        self.setXRange(0,20)
        self.setYRange(0,1)
        self.useColor=useColor
        self.setGeometry(QtCore.QRect(10, 10, 600, 600))
        self.customise_graph()
        # set default function to random data generator!!
        self.set_yield_function(self.get_data)
        # holds the refrence to the current plot
        self.data_pointer=None


        # self.gr=pg.PlotWidget()
        # self.setCentralWidget(self.gr)
        # self.gr.plot([x for x in range(20)],[x**2 for x in range(20)])
        # clearing function
        # self.clear()
        # rgb(60, 50, 33) -> stack plot secondary color (Orange)
        # rgb(37, 196, 143) -> (Green)
        # rgb(133, 59, 76) -> (Crimson Red)

        # self.show()
    #
    # def init_all(self):
    #     global seconds,values_to_show,wait_time,treshold
    #     seconds = 0
    #     values_to_show = 0
    #     wait_time = 0
    #     treshold = 0
    def set_geometry(self,lis):
        print("GEo changed!")
        self.setGeometry(QtCore.QRect(lis[0],lis[1],lis[2],lis[3]))

    def set_yield_function(self,function):
        # default yield function is aldready imported
        # the function must be passed as a reference to this widget!
        self.yielder=function

    def customise_graph(self):
        self.setBackground((32, 34, 38))


    def start_graph(self):
        self.init_settings()
        # self.t = Thread(target=self.add_point)
        # self.t.start()
        # print("After thread starting!")

    def init_settings(self):
        global values_to_show, wait_time, treshold
        # define additional settings from console
        values_to_show = 20
        wait_time = 1
        # threshold not used -> jsut switch the pens based on the condition
        treshold = 30
        self.not_killed=True
        self.red_pen = pg.mkPen(color=(255, 80, 80), width=3, style=QtCore.Qt.SolidLine)
        self.green_pen = pg.mkPen(color=(37, 196, 143), width=3, style=QtCore.Qt.SolidLine)
        self.yellow_pen = pg.mkPen(color=(185,126,10), width=3, style=QtCore.Qt.SolidLine)
        self.blue_pen = pg.mkPen(color=(9,166,212), width=3, style=QtCore.Qt.SolidLine)
        self.GREEN,self.RED,self.YELLOW,self.BLUE=(33,63,58),(49,37,42),(70,56,32),(28,57,69)
        self.CurPen=None
        if self.useColor is "G":
            self.CurPen,self.useColor=self.green_pen,self.GREEN
        elif self.useColor is "R":
            self.CurPen, self.useColor = self.red_pen, self.RED
        elif self.useColor is "B":
            self.CurPen, self.useColor = self.blue_pen, self.BLUE
        else:
            self.CurPen, self.useColor = self.yellow_pen, self.YELLOW
        # secondary green - 33,63,58
        # secondary red - 49,37,42
        # secondary yellow - 65,54,33
        # main yellow - 185,126,10
        # secondary blue - 28,57,69
        # adjusts the Y range!
        self.setYRange(1,-1)

        # optimized graph init settings
        self.values=[]
        self.values_to_show=values_to_show
        self.cnt=0
        # overflow counter
        self.ind=0
        self.wait_time=wait_time

        # plotting randm data to obtain pointer to plotItem object!
        self.data_pointer=self.plot([0],[0],pen=self.CurPen)
        # null curve to refrence for filling color using plot inbetween
        self.base_pointer=self.plot([0],[0])
        self.timer=QTimer()
        # waitime is in seconds
        self.timer.setInterval(self.wait_time*1000)
        self.timer.timeout.connect(self.optimized_graph)
        self.timer.start()




        # gradient = QLinearGradient(QPointF(0, 0), QPointF(0, 1))
        # gradient.setColorAt(0.0, QColor(60, 50, 33))
        # gradient.setColorAt(1.0, QColor(255, 128, 0))
        # gradient.setCoordinateMode(QGradient.LogicalMode)
        # self.pen.setBrush(gradient)

    def get_data(self):
        """simulator of reading values from the board"""
        # if randint(1, 100) % 2 == 0:
        #     return False, -1
        return True, ((choice([-1,1]))*np.random.random())
        # return True, self.yielder()

    def kill_graph(self):
        self.not_killed=False
        # add hardware interuppt code to kill the running graph

    def add_point(self):
        global seconds
        current_reading = 0
        times, vals = [0], []
        ind = 1
        # change back to while instead of 'if' is using threads and not Qtimer
        while (self.not_killed):
            value_read, reading = self.yielder()
            if (value_read):
                current_reading = reading
                vals.append(current_reading)
                if seconds * wait_time > 20:
                    self.setXRange(0+ind, 20+ind)
                    ind += 1
                if self.data_pointer is None:
                    self.plot(times, vals,pen=self.pen) #,symbol="o",symbolsize=30)
                else:
                    self.data_pointer.setdata(times,vals)
                print("PLot done")
                # plt.pause(0.05)
            else:
                vals.append(current_reading)
                if seconds * wait_time > 20:
                    # plt.plot(times[ind:], vals[ind:],color="blue")
                    # plt.axis([ind, values_to_show+ ind - 1, 0, 1])
                    # self.plot(times[ind:], times[:(values_to_show + ind)])
                    self.setXRange(0+ind, 20+ind)
                    ind += 1
                if self.data_pointer is None:
                    self.plot(times, vals,pen=self.pen) #,symbol="o",symbolsize=30)
                else:
                    self.data_pointer.setdata(times, vals)
                print("PLot donesdvsdvv")
                # plt.pause(0.05)

            # wait time before next reading taken
            time.sleep(wait_time)
            seconds += wait_time
            times.append(seconds)

    def optimized_graph(self):
        if self.not_killed is True:
            got,reading=self.yielder()
            self.cnt+=1
            if got:
                self.values.append(reading)
            else:
                self.values.append(self.values[-1])
            self.data_pointer.setData([x for x in range(self.cnt)],self.values)
            if len(self.values)>self.values_to_show:
                self.ind+=1
                self.setXRange(self.ind,self.values_to_show+self.ind)
            # filling base null value
            self.base_pointer.setData([x for x in range(self.cnt)],[0]*self.cnt)
            w=pg.FillBetweenItem(self.data_pointer,self.base_pointer,brush=self.useColor)
            self.addItem(w)

# app=QApplication([])
# w=Graph_demo()
# import sys
# sys.exit(app.exec_())

