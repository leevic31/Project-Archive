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

from os import path

import exportCSV
import exportPDF
import database
import query
import presetquery
import pandas as pd

class presetQueriesInterface(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()

        conn = database.get_db_connection()
        if conn.is_connected():
            print('Connected to MySQL database')
        else:
            print('Not connected to MySQL database')

        self.layout = QGridLayout(self)
        self.queries_label = QLabel('Preset Queries')
        self.cb = QComboBox()

        # NOTE THIS INTERFACE USES FUNCTIONALITY FROM PRESETQUERY.PY
        # TO RUN THIS INTERFACE YOU MUST CREATE A TABLE AS DESCRIBED
        # IN PRESETQUERY.PY AND EDIT CONFIG.PY SO THAT DATABASE CONNECTION
        # OBJECTS POINTS TO THE DATABASE CONTAINING THAT QUERY

        # finding number of preset queries
        cursor = conn.cursor()
        quer = "SELECT MAX(id) FROM Presets"
        cursor.execute(quer)
        row = cursor.fetchone()
        strrow = str(row)[1:-2]
        numvals = int(strrow)
        # looping through preset queries and adding them to combobox
        j = 1
        while j <= numvals:
            optioni = (presetquery.get_descriptin(conn, j))
            self.cb.addItem(str(j) + ") " + str(optioni))
            j += 1

        conn.close()

        # adding other elements

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
        # getting respective query based on num in description
        key = (self.cb.currentText())[:1]
        conn = database.get_db_connection()
        quer = presetquery.get_preset(conn, key)
        query_result = query.manual_sql_query(conn, quer)
        conn.close()
        # if select CSV
        if self.b1.isChecked() == True:
            # export to CSV file
            print("save as csv ", exportCSV.exportCSV(file_name, query_result))
        # else if select PDF
        elif self.b2.isChecked() == True:
            # export to PDF file
            print("save as pdf ", exportPDF.exportToPDF(file_name + '.pdf', query_result))

def main():
    app = QApplication(sys.argv)
    ex = presetQueriesInterface()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
