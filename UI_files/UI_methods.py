from PyQt5.QtCore import QPointF
from PyQt5.QtGui import QLinearGradient, QGradient
from pyqtgraph.examples.syntax import QColor

from UI_files.prototype2_UI import Ui_Dialog
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import QtCore, QtGui, QtWidgets
from UI_files.graph_demo import Graph_demo


class Main_App(Ui_Dialog, QMainWindow):
    def __init__(self):
        super(Main_App, self).__init__()
        self.setupUi(self)

        # an array to hold a reference to all the created graph objects
        # use this array to clear out the graph on quiting!
        self.created_graphs=[]


        # Gr is the only graoh created without using self.create_graph method
        self.gr = Graph_demo(self.Demo_graph)
        self.styles = {'color': 'w', 'font-size': '20px'}
        # self.gr.setLabel('left', 'Voltage (mV)',color="red",**self.styles)
        self.gr.setLabel('left', 'Voltage (mV)',color="white",size="20")
        self.gr.setLabel('bottom', 'seconds (s)',color="white")
        self.gr.start_graph()
        self.gr.set_geometry([0,0,500,500])
        # shows the grid in the graph
        self.gr.showGrid(x=True, y=True)

        self.pushButton.clicked.connect(self.clear_graph)

        # creating graph using defined methods
        self.lingr=self.create_sample_graph(self.LinDistGraph,"Time (sec)","Distance (m)")
        self.lingr.start_graph()
        self.lingrVol = self.create_sample_graph(self.LinVoltageGraph, "Time (sec)", "voltage (m)")
        self.lingrVol.start_graph()
        self.rotgr = self.create_sample_graph(self.RotGraph, "Time (sec)", "pulses ",size=[0,0,1200,330])
        self.rotgr.start_graph()


        # CLEAR_BUTTON



        # defines styling options in the graph

        # todo
        # calls and setsup the UI graph in the Tab!! -> done
        # check how to customise the graph in colors -> done
        # chech reszing options -> done
        # check livesness .... scrolling option -> Done
        # create new UI with a dedicated space for graphs with defined size!!
        # add additonal init methods here!!
        # create mutiple graphs in the same page -> done
        # create visual effects as seen in blynk graphs
        # create super imposed graphs
        # check how to create neon and gradient graphs
        # check multiple subplot creation
        # create color customisation for the graph method

        # this line connects the 'X' button to a function
        app.aboutToQuit.connect(self.wind_up)
        self.show()

    def wind_up(self):
        # added all the code to be stopped into this one
        for x in self.created_graphs:
            x.kill_graph()
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

    def clear_graph(self):
        self.gr.clear()

    def create_sample_graph(self,parent,xunit,yunit,size=[0, 0, 500, 500]):
        gr = Graph_demo(parent)
        # styles = {'color': 'w', 'font-size': '20px'}
        # self.gr.setLabel('left', 'Voltage (mV)',color="red",**self.styles)
        gr.setLabel('left', f'{yunit}', color="white", size="20")
        gr.setLabel('bottom', f'{xunit}', color="white")
        gr.showGrid(x=True, y=True)
        # gr.start_graph()
        gr.set_geometry(size)
        self.created_graphs.append(gr)
        return gr



app = QtWidgets.QApplication([])

window = Main_App()
window.setupUi(window)
window.show()

app.exec_()
