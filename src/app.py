import sys

from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget
    )

from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot, Qt

import login

class App(QMainWindow):
    def __init__(self, title='Application'):
        super().__init__()
        self.title = title
        self.left = 0
        self.top = 0
        self.width = 800
        self.height = 600
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # set up main window and widget
        self.set_main_widget(login.loginWidget(self))

    def set_main_widget(self, widget):
        self.main_widget = widget
        self.setCentralWidget(self.main_widget)
        self.show()

if __name__ == '__main__':
    qapp = QApplication(sys.argv)
    app = App()
    sys.exit(qapp.exec_())
