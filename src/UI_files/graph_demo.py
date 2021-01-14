from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QPointF, QTimer
# from PyQt5.QtGui import QLinearGradient, QColor, QGradient
from PyQt5.QtWidgets import QMainWindow, QDialog, QApplication
# import sys
# import matplotlib
# matplotlib.use('Qt5Agg')
import pyqtgraph as pg
import numpy as np
# import matplotlib.pyplot as plt
from random import randint, choice
import time
from threading import Thread

seconds, values_to_show, wait_time, treshold = 0, 0, 0, 0


class Graph_demo(pg.PlotWidget, QDialog):
    # PlotWidget are embedable in QWindows As QWidgets!!
    # TextLabel is a label that wil be passed to the graph object to update based on the value
    def __init__(self, *args, useColor="G",TextLabel=None):
        super(Graph_demo, self).__init__(*args)
        self.setXRange(0, 20)
        self.setYRange(0, 1)
        self.useColor = useColor
        self.setGeometry(QtCore.QRect(10, 10, 600, 600))
        self.customise_graph()
        self.updateLabel=TextLabel
        # set default function to random data generator
        self.set_yield_function(self.get_data)
        # holds the refrence to the current plot
        self.data_pointer = None
        # clearing function
        # self.clear()

    def set_geometry(self, lis):
        self.setGeometry(QtCore.QRect(lis[0], lis[1], lis[2], lis[3]))

    def set_yield_function(self, function):
        # default yield function is aldready imported
        # the function must be passed as a reference to this widget
        self.yielder = function

    def customise_graph(self):
        self.setBackground((32, 34, 38))

    def start_graph(self):
        self.init_settings()
        self.t = Thread(target=self.add_manual_point)
        self.t.start()
        print("After thread starting!")

    def init_settings(self):
        global values_to_show, wait_time, treshold
        # define additional settings from console
        values_to_show = 20
        wait_time = 1
        # threshold not used -> just switch the pens based on the condition
        treshold = 30
        self.not_killed = True
        self.red_pen = pg.mkPen(color=(255, 80, 80), width=3, style=QtCore.Qt.SolidLine)
        self.green_pen = pg.mkPen(color=(37, 196, 143), width=3, style=QtCore.Qt.SolidLine)
        self.yellow_pen = pg.mkPen(color=(185, 126, 10), width=3, style=QtCore.Qt.SolidLine)
        self.blue_pen = pg.mkPen(color=(9, 166, 212), width=3, style=QtCore.Qt.SolidLine)
        self.GREEN, self.RED, self.YELLOW, self.BLUE = (33, 63, 58), (49, 37, 42), (70, 56, 32), (28, 57, 69)
        self.CurPen = None
        if self.useColor is "G":
            self.CurPen, self.useColor = self.green_pen, self.GREEN
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

        # adjusts the Y range
        self.setYRange(1, -1)

        # optimized graph init settings
        self.values,self.times = [],[]
        self.values_to_show = values_to_show
        self.cnt = 0
        # overflow counter
        self.ind = 0
        self.wait_time = wait_time

        # plotting randm data to obtain pointer to plotItem object
        self.data_pointer = self.plot([0], [0], pen=self.CurPen)
        # null curve to refrence for filling color using plot inbetween
        self.base_pointer = self.plot([0], [0],pen=self.green_pen)

        # self.timer = QTimer()
        # # waitime is in seconds
        # self.timer.setInterval(self.wait_time * 1000)
        # self.timer.timeout.connect(self.optimized_graph)
        # self.timer.start()

    def get_data(self):
        """simulator of reading values from the board"""
        # if randint(1, 100) % 2 == 0:
        #     return False, -1
        return True, ((choice([-1, 1])) * np.random.random())
        # return True, self.yielder()

    def kill_graph(self):
        self.not_killed = False
        # add hardware interuppt code to kill the running graph

    def optimized_graph(self):
        if self.not_killed is True:
            got, reading = self.yielder()
            self.cnt += 1
            if got:
                self.values.append(reading)
            else:
                self.values.append(self.values[-1])
            self.data_pointer.setData([x for x in range(self.cnt)], self.values)
            if len(self.values) > self.values_to_show:
                self.ind += 1
                self.setXRange(self.ind, self.values_to_show + self.ind)
            # draws a straight white line along thhe X-axis
            self.base_pointer.setData([x for x in range(self.cnt)], [0] * self.cnt)
            # filling function to plot between X-axis line and data curve
            w = pg.FillBetweenItem(self.data_pointer, self.base_pointer, brush=self.useColor)
            self.addItem(w)
            if self.updateLabel is not None:
                self.updateLabel.setText(str(reading)[:5])

    def add_manual_point(self):
        # use 1 as data for rotary encoder and float value of reading for the linear encoder
        # tested and works like a charm
        # graph plotting doesn't work check that!!
        prev=1
        while(self.not_killed):
            value_read,(time,data)=self.yielder()
            print(time,data)
            # data=data[0]
            if time!=prev:
                self.times.append(time)
                self.values.append(data)
                print(self.times)
                self.data_pointer.setData(self.times, self.values)
                self.base_pointer.setData(self.times, [0]*len(self.values))
                if len(self.times)>=self.values_to_show:
                    self.times.pop(0)
                    self.values.pop(0)
                prev=time




# app=QApplication([])
# w=Graph_demo()
# w.start_graph()
# w.show()
# import sys
# for x in range(10):
#     w.add_manual_point(0.6+x,x)
#     time.sleep(1)
# sys.exit(app.exec_())
