from PyQt5.QtWidgets import (
    QAction,
    QApplication,
    QGridLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QTabWidget,
    QWidget,
    )

from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot, Qt

import login

class AdministrativeWidget(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__()
        self.parent = parent
        self._setup_widget()

    def _setup_widget(self):
        self.logoutBtn = QPushButton("Logout")
        self.logoutBtn.clicked.connect(self.onClick)

        self.layout = QGridLayout(self)
        self.layout.addWidget(self.logoutBtn, 0, 0)

        self.setLayout(self.layout)

    @pyqtSlot()
    def onClick(self):
        self.parent.set_main_widget(login.loginWidget(self.parent))
        self.close()
