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

import sys

import database
import exportCSV
import exportPDF
import query
import gui_helper

class ModifyPresetQueryWidget(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()
        self._setup_widget()

    def _setup_widget(self):
        self.query = QTextEdit(self)
        self.label = QLabel("Query:")
        self.modify_options = {
            "add",
            "remove"
            }
        self.modify_combobox = QComboBox()
        for key in self.modify_options:
            self.modify_combobox.addItem(key)
        self.modify = QPushButton("Enter")
        
        self.layout = QGridLayout(self)
        self.layout.setColumnStretch(0, 2)
        
        self.layout.addWidget(self.label, 0, 0)
        self.layout.addWidget(self.query, 1, 0)
        self.layout.addWidget(self.modify_combobox, 1, 1)
        self.layout.addWidget(self.modify, 2, 1)
        self.setLayout(self.layout)
        
if (__name__ == "__main__"):
    app = QApplication(sys.argv)
    ex = ModifyPresetQueryWidget()
    ex.show()
    sys.exit(app.exec_())