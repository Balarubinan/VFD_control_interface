from UI_files.prototype_UI import Ui_Dialog
from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5 import QtCore, QtGui, QtWidgets



class Main_App(Ui_Dialog,QMainWindow):
    def __init__(self):
        super(Main_App, self).__init__()
        self.setupUi(self)
        # add additonal init methods here!!
        self.show()

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

