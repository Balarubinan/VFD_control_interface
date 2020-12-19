from PyQt5 import QtCore, QtGui, QtWidgets
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
        self.setXRange(0,100)
        self.setYRange(0,100)
        self.setGeometry(QtCore.QRect(10,10,500,500))

        # self.gr=pg.PlotWidget()
        # self.setCentralWidget(self.gr)
        # self.gr.plot([x for x in range(20)],[x**2 for x in range(20)])

        # self.show()
    #
    # def init_all(self):
    #     global seconds,values_to_show,wait_time,treshold
    #     seconds = 0
    #     values_to_show = 0
    #     wait_time = 0
    #     treshold = 0
    def start_graph(self):
        self.init_settings()
        self.t = Thread(target=self.add_point)
        self.t.start()

    def init_settings(self):
        global values_to_show, wait_time, treshold
        # define additional settings from console
        values_to_show = 20
        wait_time = 1
        treshold = 30

    def get_data(self):
        """simulator of reading values from the board"""
        if randint(1, 100) % 2 == 0:
            return False, -1
        return True, np.random.random()
        # return True, yielder()

    def kill_graph(self):
        pass
        # add hardware interuppt code to kill the running graph

    def add_point(self):
        global seconds
        current_reading = 0
        times, vals = [0], []
        ind = 1
        while (True):
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
                    ind += 1

                self.plot(times, vals)
                print("PLot done")
                # plt.pause(0.05)
            else:
                vals.append(current_reading)
                if seconds * wait_time > 20:
                    # plt.plot(times[ind:], vals[ind:],color="blue")
                    # plt.axis([ind, values_to_show+ ind - 1, 0, 1])
                    # self.plot(times[ind:], times[:(values_to_show + ind)])

                    ind += 1

                self.plot(times, vals)
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

