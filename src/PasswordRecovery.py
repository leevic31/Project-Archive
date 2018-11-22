import sys
from PyQt5.QtWidgets import QDialog, QWidget, QPushButton, QAction, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot, Qt

import gui_helper
from emailAPI import *

# used https://pythonspot.com/pyqt5-textbox-example/ as reference to setup the UI
class Password_Recovery(QDialog):
    def __init__(self, parent):
        super(QDialog, self).__init__(parent)
        self.title = 'Password Recovery'
        self.left = 10
        self.top = 10
        self.width = 400
        self.height = 140
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Create textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20)
        self.textbox.resize(280,40)

        # Create a button in the window
        self.button = QPushButton('Send', self)
        self.button.move(20,80)

        # connect button to function on_click
        self.button.clicked.connect(self.on_click)
        self.setWindowModality(Qt.ApplicationModal)
        self.exec_()

    @pyqtSlot()
    def on_click(self):
        textboxValue = self.textbox.text()
        if ('@' not in textboxValue or '.' not in textboxValue):
            gui_helper.prompt_error("Please enter a valid email")
            return
        # check if given email exists in agency db
        password = database.get_user_password
        if(password is None):
            gui_helper.prompt_error("Please enter a valid email")
            return
        QMessageBox.question(self, 'Message', "Check " +  textboxValue + " for your login information", QMessageBox.Ok, QMessageBox.Ok)
        self.textbox.setText("")
        sendEmail(self, textboxValue, password)
        self.done(0)
