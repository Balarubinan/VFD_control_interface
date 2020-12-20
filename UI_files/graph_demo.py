from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QPointF
from PyQt5.QtGui import QLinearGradient, QColor, QGradient
from PyQt5.QtWidgets import QMainWindow,QDialog,QApplication
import sys
import matplotlib
matplotlib.use('Qt5Agg')
import pyqtgraph as pg
import numpy as np
import matplotlib.pyplot as plt
from random import randint
import time
from threading import Thread

seconds,values_to_show,wait_time,treshold=0,0,0,0

class Graph_demo(pg.PlotWidget,QDialog):
    # Qdialogs are mebedable in QWindows As QWidgets!!
    def __init__(self,*args):
        super(Graph_demo, self).__init__(*args)
        self.setXRange(0,20)
        self.setYRange(0,1)
        self.setGeometry(QtCore.QRect(10, 10, 600, 600))
        self.customise_graph()

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
        self.t = Thread(target=self.add_point)
        self.t.start()
        print("After thread starting!")

    def init_settings(self):
        global values_to_show, wait_time, treshold
        # define additional settings from console
        values_to_show = 20
        wait_time = 1
        treshold = 30
        self.not_killed=True
        self.pen = pg.mkPen(color=(255, 80, 80), width=3, style=QtCore.Qt.SolidLine)
        self.pen2 = pg.mkPen(color=(37, 196, 143), width=3, style=QtCore.Qt.SolidLine)
        self.pen3 = pg.mkPen(color=(60, 50, 33), width=3, style=QtCore.Qt.SolidLine)

        # gradient = QLinearGradient(QPointF(0, 0), QPointF(0, 1))
        # gradient.setColorAt(0.0, QColor(60, 50, 33))
        # gradient.setColorAt(1.0, QColor(255, 128, 0))
        # gradient.setCoordinateMode(QGradient.LogicalMode)
        # self.pen.setBrush(gradient)

    def get_data(self):
        """simulator of reading values from the board"""
        if randint(1, 100) % 2 == 0:
            return False, -1
        return True, np.random.random()
        # return True, self.yielder()

    def kill_graph(self):
        self.not_killed=False
        # add hardware interuppt code to kill the running graph

    def add_point(self):
        global seconds
        current_reading = 0
        times, vals = [0], []
        ind = 1
        while (self.not_killed):
            value_read, reading = self.get_data()
            if (value_read):
                current_reading = reading
                vals.append(current_reading)
                if seconds * wait_time > 20:
                    # plt.plot(times[ind:], vals[ind:],color="blue")
                    # plotting only the last values_to_show number of  values using list slicing
                    # plt.axis([ind, values_to_show + ind - 1, 0, 1])
                    # self.plot(times[ind:], times[:(values_to_show + ind)])
                    # plt.fill_between(x, y)
                    # auto scroll is achived by the below statement
                    self.setXRange(0+ind, 20+ind)
                    ind += 1

                self.plot(times, vals,pen=self.pen) #,symbol="o",symbolsize=30)
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

                self.plot(times, vals,pen=self.pen) #,symbol="o",symbolsize=30)
                print("PLot donesdvsdvv")
                # plt.pause(0.05)

            # wait time before next reading taken
            time.sleep(wait_time)
            seconds += wait_time
            times.append(seconds)


# app=QApplication([])
# w=Graph_demo()
# import sys
# sys.exit(app.exec_())

