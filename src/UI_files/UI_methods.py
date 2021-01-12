from src.UI_files.prototype2_UI import Ui_Dialog
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtWidgets
from src.UI_files.graph_demo import Graph_demo
from requests import get
from Flask_server_files.simulator import get_values


class Main_App(Ui_Dialog, QMainWindow):
    def __init__(self):
        super(Main_App, self).__init__()
        self.setupUi(self)

        # an array to hold a reference to all the created graph objects
        # use this array to clear out the graph on quiting!
        self.created_graphs=[]


        # Gr is the only graoh created without using self.create_graph method
        self.gr = self.create_sample_graph(self.Demo_graph,"Voltage (V)","Time (sec)")
        # uncomment this part to use the actual values from the server
        # self.gr.set_yield_function(self.get_lin_values)
        self.gr.start_graph()


        # shows the grid in the graph
        self.gr.showGrid(x=True, y=True)

        self.pushButton.clicked.connect(self.clear_graph)

        # creating graph using defined methods
        self.lingr=self.create_sample_graph(self.LinDistGraph,"Time (sec)","Distance (m)",Txtlabel=self.DistanceLabel)
        # uncomment to use actual value
        # self.lingr.set_yield_function(self.get_lin_values)
        self.lingr.start_graph()
        self.lingrVol = self.create_sample_graph(self.LinVoltageGraph, "Time (sec)", "voltage (m)",color="Y")
        self.lingrVol.start_graph()
        self.rotgr = self.create_sample_graph(self.RotGraph, "Time (sec)", "pulses ",size=[0,0,1200,330],color="B")
        self.rotgr.set_yield_function(get_values)
        self.rotgr.start_graph()


        # CLEAR_BUTTON



        # defines styling options in the graph

        # todo
        # create new UI with a dedicated space for graphs with defined size!!
        # create super imposed graphs ?? do we need it??
        # create a direct socket connection to the server to send and recieve rotary encoder data
        # rotary encoder data needs to be instantaneous!!

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

    def create_sample_graph(self,parent,xunit,yunit,size=[0, 0, 591, 451],color="G",Txtlabel=None):
        gr = Graph_demo(parent,useColor=color,TextLabel=Txtlabel)
        # styles = {'color': 'w', 'font-size': '20px'}
        # self.gr.setLabel('left', 'Voltage (mV)',color="red",**self.styles)
        gr.setLabel('left', f'{yunit}', color="white", size="20")
        gr.setLabel('bottom', f'{xunit}', color="white")
        gr.showGrid(x=True, y=True)
        # gr.start_graph()
        gr.set_geometry(size)
        self.created_graphs.append(gr)
        return gr

    def get_lin_values(self):
        val = get("http://balarubinan.pythonanywhere.com/lin/23")
        return True,val.json()['reading']



app = QtWidgets.QApplication([])

window = Main_App()
window.setupUi(window)
window.show()

app.exec_()
