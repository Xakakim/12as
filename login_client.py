from login import Ui_MainWindow
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QInputDialog
from asyncqt import QEventLoop
from pyrogram import Client
import asyncio
import sys

from_main = ("main_client.py")[0]

class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()


    
    def loginChk(self):
        api_id = int(self.Api.text())
        api_hash = self.Hash.text()
        phone_number = self.Phone.text()
        client = Client("my_account", api_id, api_hash)
        client.connect()
        sent_code_info = client.send_code(phone_number)
        (phone_code, ) = input (QInputDialog.getText(self , 'Input Dialog' , 'Enter your Code:'))
        client.sign_in(phone_number, sent_code_info.phone_code_hash, phone_code)





app = QtWidgets.QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())
