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

import password_recovery_interface
import gui_helper
import agency_ui
import teq_ui

class loginWidget(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.parent = parent
        self.layout = QGridLayout(self)

        self.username_label = QLabel("Username:")
        self.username_field = QLineEdit(self)
        self.password_label = QLabel("Password:")
        self.password_field = QLineEdit(self)
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

    def set_agency_ui(self):
        self.parent.main_widget = agency_ui.agencyWidget(self)
        self.parent.setCentralWidget(self.parent.main_widget)
        self.parent.show()

    def set_teq_ui(self):
        self.parent.main_widget = teq_ui.teqWidget(self)
        self.parent.setCentralWidget(self.parent.main_widget)
        self.parent.show()

    @pyqtSlot()
    def login(self):
        username = self.username_field.text()
        # if login is correct
        if (username == "agency"):
            self.set_agency_ui()
        elif (username == "teq"):
            self.set_teq_ui()
        else:
            gui_helper.prompt_error("Wrong username or password")
        
    @pyqtSlot()
    def recoverPassword(self):
        password_recovery_interface.Password_Recovery(self)
