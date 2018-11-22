from PyQt5.QtWidgets import (
    QAction,
    QApplication,
    QComboBox,
    QDialog,
    QGridLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QVBoxLayout,
    QWidget
    )

from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot, Qt

import gui_helper
import TeqWidget
import PasswordRecovery

from AgencyUploadWidget import *
from TeqQueryWidget import *
from PresetQueryWidget import *

class loginWidget(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.parent = parent
        self.layout = QGridLayout(self)

        self.username_label = QLabel("Username:")
        self.username_field = QLineEdit(self)
        self.password_label = QLabel("Password:")
        self.password_field = QLineEdit(self)
        self.password_field.setEchoMode(QLineEdit.Password)
        self.submit = QPushButton("Login")
        self.submit.clicked.connect(self.login)

        self.recover_button = QPushButton("Recover Password")
        self.recover_button.clicked.connect(self.recoverPassword)

        self.layout.addWidget(self.username_label, 0, 0)
        self.layout.addWidget(self.username_field, 0, 1)
        self.layout.addWidget(self.password_label, 1, 0)
        self.layout.addWidget(self.password_field, 1, 1)
        self.layout.addWidget(self.submit, 2, 1)
        self.layout.addWidget(self.recover_button, 3, 1)
        self.setLayout(self.layout)

    def set_main_widget(self, widget):
        self.parent.main_widget = widget
        self.parent.setCentralWidget(self.parent.main_widget)
        self.parent.show()

    def set_agency_ui(self):
        widget = TeqWidget.teqWidget(self)
        widget.add_widget(iCareUploadWidget(), "Upload iCare Data")
        self.set_main_widget(widget)

    def set_teqhigh_ui(self):
        widget = TeqWidget.teqWidget(self)
        widget.add_widget(iCareNewQueryWidget(), "Run custom query")
        widget.add_widget(presetQueriesInterface(), "Run Reports")
        self.set_main_widget(widget)

    def set_teqlow_ui(self):
        widget = TeqWidget.teqWidget(self)
        widget.add_widget(presetQueriesInterface(), "Run Reports")
        self.set_main_widget(widget)


    @pyqtSlot()
    def login(self):
        username = self.username_field.text()
        # get user type
        user_type = None
        # if login is correct
        if (username == "agency"):
            self.set_agency_ui()
        elif (username == "teqhigh"):
            self.set_teqhigh_ui()
        elif (username == "teqlow"):
            self.set_teqlow_ui()
        else:
            gui_helper.prompt_error("Wrong username or password")

    @pyqtSlot()
    def recoverPassword(self):
        PasswordRecovery.Password_Recovery(self)
