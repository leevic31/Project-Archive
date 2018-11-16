import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QFileDialog,
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
import gui_helper
import query
import presetquery
import pandas as pd

class presetQueriesInterface(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()

        self.layout = QGridLayout(self)
        self.layout.setColumnStretch(0, 1)
        self.layout.setColumnStretch(1, 3)

        self.queries_label = QLabel('Preset Queries')
        self.cb = QComboBox()

        self.preset_queries = database.get_preset_queries()
        for _id, query, desc in self.preset_queries:
            self.cb.addItem(desc)

        # adding other elements

        self.export_options = {
                "csv": exportCSV.ExportCSV(),
                "pdf": exportPDF.ExportPDF()
                }
        self.export_combobox = QComboBox()
        for key in self.export_options:
            self.export_combobox.addItem(key)

        self.generate = QPushButton("Generate", self)
        self.generate.clicked.connect(self.on_click)

        self.layout.addWidget(self.queries_label, 0, 0)
        self.layout.addWidget(self.cb, 0, 1)
        self.layout.addWidget(self.export_combobox, 1, 1)
        self.layout.addWidget(self.generate, 3, 1)
        self.setLayout(self.layout)

    @pyqtSlot()
    def on_click(self):
        # show file dialog for user to name their file
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.AnyFile)
        if dialog.exec_():
            filepaths = dialog.selectedFiles()
            file_name = filepaths[0]

            # get the index of selected preset query
            index = self.cb.currentIndex()
            # get query at that index
            quer = self.preset_queries[index][1]

            # get selected export option
            export_option = self.export_options[self.export_combobox.currentText()]

            try:
                export_option.export(file_name, quer)
                gui_helper.prompt_information("Data has been succesfully exported!")
            except Exception as e:
                gui_helper.prompt_error("Failed to export data: " + str(e))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = presetQueriesInterface()
    ex.show()
    sys.exit(app.exec_())
