import sys
#from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QLabel
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QSize

class Agency(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = "Enter the information required to add a new Agency"
        self.setMinimumSize(QSize(500, 500))
        self.left = 100
        self.top = 100
        self.width = 700
        self.height = 700
        self.agencyWindow()

    def agencyWindow(self):
        self.name = QLineEdit(self)
        self.name.setPlaceholderText("Agency Name ...")
        self.name.setGeometry(200,100,200,30)

        self.address = QLineEdit(self)
        self.address.setPlaceholderText("Agency Address ...")
        self.address.setGeometry(200,150,200,30)

        self.numEmployees = QLineEdit(self)
        self.numEmployees.setPlaceholderText("Number of employees ...")
        self.numEmployees.setGeometry(200,200,200,30)

        self.iCareTemplate = QLineEdit(self)
        self.iCareTemplate.setPlaceholderText("Choice of iCARE template ...")
        self.iCareTemplate.setGeometry(200,250,200,30)

        self.button = QPushButton("Add", self)
        self.button.setGeometry(250,300,100,30)

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()


if __name__ == '__main__':
    my_app = QApplication(sys.argv)
    agency = Agency()
    sys.exit(my_app.exec_())
