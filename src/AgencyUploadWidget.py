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
    QSpinBox,
    QTabWidget,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget
    )

from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot, Qt

import sys

import pyxl
import database
import gui_helper

def get_file_name(path : str) -> str:
    return path[path.rfind("/") + 1:]

class iCareUploadWidget(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()
        self.filepaths = []
        self._setup_widget()

    def _setup_widget(self):
        # set layouts
        self.layout = QGridLayout(self)
        self.layout.setColumnStretch(0, 1)
        self.layout.setColumnStretch(2, 3)

        self.file_upload_label = QLabel("No File Chosen")
        self.upload1 = QPushButton("Select Data")
        self.upload1.clicked.connect(self.file_select)
        self.submit1 = QPushButton("Submit Data")
        self.submit1.clicked.connect(self.submit_iCare_data)

        self.minbound_label = QLabel("start row number:")
        self.minbound = QSpinBox()
        self.minbound.setValue(4)
        self.minbound.setMinimum(1)

        self.maxbound_label = QLabel("stop row number:")
        self.maxbound = QSpinBox()
        self.maxbound.setValue(5)
        self.maxbound.setMinimum(1)

        # widgets
        self.iCare_combobox = QComboBox()
        try:
            self.iCare_types = database.get_iCare_template_names()
            for iCare_type in self.iCare_types:
                self.iCare_combobox.addItem(iCare_type)
        except Exception as e:
            gui_helper.prompt_error("Failed to get Templates: " + str(e))


        self.layout.addWidget(QLabel("iCare format data for:"), 0, 0)
        self.layout.addWidget(self.iCare_combobox, 0, 1, 1, 5)
        self.layout.addWidget(self.upload1, 1, 0)
        self.layout.addWidget(self.file_upload_label, 1, 1)
        self.layout.addWidget(self.minbound_label, 2, 0)
        self.layout.addWidget(self.minbound, 2, 1)
        self.layout.addWidget(self.maxbound_label, 3, 0)
        self.layout.addWidget(self.maxbound, 3, 1)
        self.layout.addWidget(self.submit1, 4, 0)

        self.setLayout(self.layout)

    @pyqtSlot()
    def file_select(self):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.AnyFile)
        dialog.setNameFilter("xlsx (*.xlsx)")

        if dialog.exec_():
            self.filepaths = dialog.selectedFiles()
            self.file_upload_label.setText(get_file_name(self.filepaths[0]))

    @pyqtSlot()
    def submit_iCare_data(self):
        if (not self.filepaths):
            gui_helper.prompt_error("Please select an xlsx file")
            return
        template_name = self.iCare_combobox.currentText()
        if (not template_name):
            gui_helper.prompt_error("Please select a type")
            return

        row_start = self.minbound.value()
        row_end = self.maxbound.value()

        try:
            database.insert_data_for(template_name, self.filepaths[0], row_start, row_end)
            gui_helper.prompt_information("Data has been successfully added to the database")
        except Exception as e:
            gui_helper.prompt_error(str(e))

if (__name__ == "__main__"):
    app = QApplication(sys.argv)
    ex = iCareUploadWidget()
    ex.show()
    sys.exit(app.exec_())

