import asyncio
from asyncqt import QEventLoop
from pyrogram import Client
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox, QInputDialog
from PyQt5.QtCore import QTimer
from PyQt5 import QtWidgets
from main import Ui_Form
import sys






class Example(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.timer = QTimer()
        self.timer.timeout.connect(self.chk)
        self.timer.setInterval(5 * 60 * 1000)
        self.time_btn_5m.setChecked(True)
        self.show()



    def setCycle(self):
        if self.time_btn_5m.isChecked():
            self.timer.setInterval(5*60*1000)
        elif self.time_btn_10m.isChecked():  
            self.timer.setInterval(10*60*1000)
        elif self.time_btn_30m.isChecked():  
            self.timer.setInterval(30*60*1000)
        elif self.time_btn_1h.isChecked(): 
            self.timer.setInterval(60*60*1000)
        elif self.time_btn_3h.isChecked(): 
            self.timer.setInterval(180*60*1000)


    def startChk(self):
        pass


    def stopChk(self):
        pass


    def chk(self):
        pass



app = QtWidgets.QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())
