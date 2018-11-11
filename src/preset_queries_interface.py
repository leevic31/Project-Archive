import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QComboBox,
    QPushButton,
    QMessageBox,
    QRadioButton,
    QGridLayout,
    QLabel,
    QLineEdit
    )
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import exportFile
import exportPDF
import database
import query
from os import path
import pandas as pd
import NameReport
class presetQueriesInterface(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()
    
        self.layout = QGridLayout(self)
        self.queries_label = QLabel('Preset Queries')
        self.cb = QComboBox()
        # TODO: add preset queries to QComboBox
        self.cb.addItem("option1")
        self.cb.addItem("option2")
        
        self.b1 = QRadioButton("CSV")
        self.b1.setChecked(True)        
        
        self.b2 = QRadioButton("PDF")
        
        self.fileName_label = QLabel("Save file name as:")
        self.fileName_field = QLineEdit(self)
        
        self.generate = QPushButton("Generate", self)
        self.generate.clicked.connect(self.on_click)

        self.layout.addWidget(self.queries_label, 0, 0)
        self.layout.addWidget(self.cb, 0, 1)
        self.layout.addWidget(self.b1, 1, 0)
        self.layout.addWidget(self.b2, 1, 1)        
        self.layout.addWidget(self.fileName_label, 2, 0)
        self.layout.addWidget(self.fileName_field, 2, 1)
        self.layout.addWidget(self.generate, 3, 1)
        self.setLayout(self.layout)
    
    @pyqtSlot()
    def on_click(self):
        file_name = self.fileName_field.text()
        # if select CSV
        if self.b1.isChecked() == True:
            # export to CSV file
            exportFile.exportCSV(file_name, query_result)
        # else if select PDF
        elif self.b2.isChecked() == True:
          
            # export to PDF file
            exportPDF.exportToPDF(file_name + '', query_result)

        
def main():
    app = QApplication(sys.argv)
    ex = presetQueriesInterface()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()