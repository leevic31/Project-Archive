from PyQt5.QtWidgets import (
    QAction,
    QApplication,
    QComboBox,
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

        self._setup_template_combobox()

        self.layout.addWidget(QLabel("iCare format data for:"), 0, 0)
        self.layout.addWidget(self.iCare_combobox, 0, 1, 1, 5)
        self.layout.addWidget(self.upload1, 1, 0)
        self.layout.addWidget(self.file_upload_label, 1, 1)
        self.layout.addWidget(self.submit1, 4, 0)

        self.setLayout(self.layout)

    def _setup_template_combobox(self):
        self.iCare_combobox = QComboBox()
        try:
            self.iCare_types = database.get_iCare_template_names()
            for iCare_type in self.iCare_types:
                self.iCare_combobox.addItem(iCare_type)
        except Exception as e:
            gui_helper.prompt_error("Failed to get Templates: " + repr(e))

    @pyqtSlot()
    def file_select(self):
        self.filepaths = gui_helper.prompt_file_chooser()
        self.file_upload_label.setText("{} files selected".format(len(self.filepaths)))

    @pyqtSlot()
    def submit_iCare_data(self):
        if (not self.filepaths):
            gui_helper.prompt_error("Please select an xlsx file")
            return
        template_name = self.iCare_combobox.currentText()
        if (not template_name):
            gui_helper.prompt_error("Please select a type")
            return

        for filepath in self.filepaths:
            try:
                database.insert_iCare_data(template_name, filepath)
            except Exception as e:
                gui_helper.prompt_error(repr(e))
                return

        gui_helper.prompt_information("Data has been successfully added to the database")

if (__name__ == "__main__"):
    app = QApplication(sys.argv)
    ex = iCareUploadWidget()
    ex.show()
    sys.exit(app.exec_())
