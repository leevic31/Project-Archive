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

def get_file_name(path : str) -> str:
    return path[path.rfind("/") + 1:]

class agencyWidget(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QGridLayout(self)

        # Initialize tab screen
        self.tab_widget = QTabWidget()
#        self.tabs = [iCareNewTemplateWidget(), iCareUploadWidget()]

#        self.tab_widget.addTab(self.tabs[0], "Add New Template")
#        self.tab_widget.addTab(self.tabs[1], "Upload iCare Data")

        self.tabs = [iCareUploadWidget()]

        self.tab_names = ["Upload iCare Data"]
        for i in range(len(self.tabs)):
            self.tab_widget.addTab(self.tabs[i], self.tab_names[i])

        self.layout.addWidget(self.tab_widget)
        self.setLayout(self.layout)

