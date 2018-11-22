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
    QTableWidget,
    QTableWidgetItem,
    QTextEdit,
    QVBoxLayout,
    QWidget
    )

from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot, Qt

import pyxl
import database
from gui_helper import (
    prompt_error,
    prompt_information
    )

def get_file_name(path : str) -> str:
    return path[path.rfind("/") + 1:]

class teqWidget(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QGridLayout(self)

        self.tab_widget = QTabWidget()

        self.layout.addWidget(self.tab_widget)
        self.setLayout(self.layout)

    def add_widget(self, widget, name):
        self.tab_widget.addTab(widget, name)

