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
    QVBoxLayout,
    QWidget
    )

from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot, Qt

from AgencyUploadWidget import *

class agencyWidget(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QGridLayout(self)

        # Initialize tab screen
        self.tab_widget = QTabWidget()

        self.tabs = [
                     (iCareUploadWidget(), "Upload iCare Data"),
                    ]

        for (widget, name) in self.tabs:
            self.tab_widget.addTab(widget, name)

        self.layout.addWidget(self.tab_widget)
        self.setLayout(self.layout)

