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

import pyxl
from gui_helper import (
    prompt_error,
    prompt_information
    )

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

class iCareUploadWidget(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()
        self.filepaths = []
        self._setup_widget()

    def _setup_widget(self):
        # set layouts
        self.layout = QGridLayout(self)
        self.layout.setColumnStretch(0, 1)
        self.layout.setColumnStretch(1, 3)


        # widgets
        self.iCare_combobox = QComboBox()
        self.iCare_types = pyxl.get_iCare_template_names()
        for iCare_type in self.iCare_types:
            self.iCare_combobox.addItem(iCare_type)

        self.file_upload_label = QLabel("No File Chosen")
        self.upload1 = QPushButton("Select Data")
        self.upload1.clicked.connect(self.file_select)
        self.submit1 = QPushButton("Submit Data")
        self.submit1.clicked.connect(self.submit_iCare_data)

        self.layout.addWidget(QLabel("iCare format data for:"), 0, 0)
        self.layout.addWidget(self.iCare_combobox, 0, 1)
        self.layout.addWidget(self.upload1, 1, 0)
        self.layout.addWidget(self.file_upload_label, 1, 1)
        self.layout.addWidget(self.submit1, 2, 0)
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
            prompt_error("Please select an xlsx file")
            return
        template_name = self.iCare_combobox.currentText()
        if (not template_name):
            prompt_error("Please select a type")
            return

        print("inserting data for", template_name)

        pyxl.insert_data_for(template_name, self.filepaths[0])

