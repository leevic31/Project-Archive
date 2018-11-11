import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QSize
# import db_config
import mysql.connector
from mysql.connector import MySQLConnection, Error
from dbsetup import db_connection, add_agency


class Agency(QWidget):

    def __init__(self):
        super().__init__()
        # Window title
        self.title = "Enter the information required to add a new Agency"
        # Window dimensions for the min size
        self.setMinimumSize(QSize(500, 500))
        # Actual dimensions of window
        self.left = 100
        self.top = 100
        self.width = 700
        self.height = 700
        self.agencyWindow()
        self.dbsetup.db_connection()
        self.dbsetup.add_agency()

    def agencyWindow(self):
        # Set the title of the window as defined in __init__
        self.setWindowTitle(self.title)
        # Set the geometry of the window as defined in in __init__
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Data entry for Agency Name
        self.name = QLineEdit(self)
        self.name.setPlaceholderText("Agency Name ...")
        self.name.setGeometry(200,100,200,30)

        # Data entry for Agency Address
        self.address = QLineEdit(self)
        self.address.setPlaceholderText("Agency Address ...")
        self.address.setGeometry(200,150,200,30)

        # Data entry for the number of employees in an agency
        self.numEmployees = QLineEdit(self)
        self.numEmployees.setPlaceholderText("Number of employees ...")
        self.numEmployees.setGeometry(200,200,200,30)

        # Data entry for the choice of the iCareTemplate used by agency
        self.iCareTemplate = QLineEdit(self)
        self.iCareTemplate.setPlaceholderText("Choice of iCARE template ...")
        self.iCareTemplate.setGeometry(200,250,200,30)

        # Button to add the agency to db
        self.button = QPushButton("Add", self)
        self.button.setGeometry(250,300,100,30)


        self.show()



if __name__ == '__main__':
    my_app = QApplication(sys.argv)
    agency = Agency()
    sys.exit(my_app.exec_())
