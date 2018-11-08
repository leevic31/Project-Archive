import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

from emailAPI import *
# used https://pythonspot.com/pyqt5-textbox-example/ as reference to setup the UI
class Password_Recovery(QMainWindow):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
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
        self.show()
 
    @pyqtSlot()
    def on_click(self):
        textboxValue = self.textbox.text()
        QMessageBox.question(self, 'Message', "Check " +  textboxValue + " for your login information", QMessageBox.Ok, QMessageBox.Ok)
        self.textbox.setText("")
        sendEmail(self, textboxValue)
 
#if __name__ == '__main__':
    #app = QApplication(sys.argv)
    #ex = Password_Recovery()
    #sys.exit(app.exec_())