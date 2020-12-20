from PyQt5.QtCore import QPointF
from PyQt5.QtGui import QLinearGradient, QGradient
from pyqtgraph.examples.syntax import QColor

from UI_files.prototype_UI import Ui_Dialog
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import QtCore, QtGui, QtWidgets
from UI_files.graph_demo import Graph_demo


class Main_App(Ui_Dialog, QMainWindow):
    def __init__(self):
        super(Main_App, self).__init__()
        self.setupUi(self)

        self.gr = Graph_demo(self.VFDControlTab)
        self.styles = {'color': 'w', 'font-size': '20px'}
        # self.gr.setLabel('left', 'Voltage (mV)',color="red",**self.styles)
        self.gr.setLabel('left', 'Voltage (mV)',color="white",size="20")
        self.gr.setLabel('bottom', 'seconds (s)',color="white")
        self.gr.start_graph()
        self.gr.set_geometry([100,50,600,600])


        # shows the grid in the graph
        self.gr.showGrid(x=True, y=True)

        # defines styling options in the graph

        # todo
        # calls and setsup the UI graph in the Tab!! -> done
        # check how to customise the graph in colors -> done
        # chech reszing options -> done
        # check livesness .... scrolling option -> Done
        # create new UI with a dedicated space for graphs with defined size!!
        # add additonal init methods here!!
        # create mutiple graphs in the same page
        # create visual effects as seen in blynk graphs
        # create super imposed graphs
        # check how to create neon and gradient graphs
        # check multiple subplot creation

        # this line connects the 'X' button to a function
        app.aboutToQuit.connect(self.wind_up)
        self.show()

    def wind_up(self):
        # added all the code to be stopped into this one
        self.gr.kill_graph()
        print("Graph killed")

    def lin_control(self):
        pass

    def VFD_control(self):
        pass

    def rot_control(self):
        pass

    def rot_graph(self):
        pass

    def lin_graph(self):
        pass

    def VFD_graph(self):
        pass


app = QtWidgets.QApplication([])

window = Main_App()
window.setupUi(window)
window.show()

app.exec_()
