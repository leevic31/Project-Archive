from PyQt5.QtWidgets import (
    QAction,
    QApplication,
    QComboBox,
    QDialog,
    QFileDialog,
    QGridLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QTabWidget,
    QVBoxLayout,
    QWidget
    )

from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot, Qt
import password_recovery_interface
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
        
        self.button1 = QPushButton("Recover Password")
        self.button1.clicked.connect(self.recoverPassword)
        

        self.layout.addWidget(self.username_label, 0, 0)
        self.layout.addWidget(self.username_field, 0, 1)
        self.layout.addWidget(self.password_label, 1, 0)
        self.layout.addWidget(self.password_field, 1, 1)
        self.layout.addWidget(self.submit, 2, 1)
        self.layout.addWidget(self.button1, 2, 2)
        self.setLayout(self.layout)

    @pyqtSlot()
    def login(self):
        # if login is correct

        self.parent.set_agency_ui()
        
    @pyqtSlot()
    def recoverPassword(self):
        self.parent.recover_password()

