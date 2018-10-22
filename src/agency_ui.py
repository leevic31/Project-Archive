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
    QVBoxLayout,
    QWidget
    )

from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot, Qt

import pyxl

def get_file_name(path : str) -> str:
    return path[path.rfind("/") + 1:]

def prompt_error(message, title="Error"):
        messagebox = QMessageBox()
        messagebox.setIcon(QMessageBox.Critical)
        messagebox.setText(message)
        messagebox.setStandardButtons(QMessageBox.Close)
        messagebox.setWindowTitle(title)
        messagebox.setWindowModality(Qt.ApplicationModal)
        messagebox.exec_()

def prompt_information(message, title="Notice"):
        messagebox = QMessageBox()
        messagebox.setIcon(QMessageBox.Information)
        messagebox.setText(message)
        messagebox.setStandardButtons(QMessageBox.Close)
        messagebox.setWindowTitle(title)
        messagebox.setWindowModality(Qt.ApplicationModal)
        messagebox.exec_()

class agencyWidget(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QGridLayout(self)

        # Initialize tab screen
        self.tab_widget = QTabWidget()
        self.tabs = [iCareNewTemplateWidget(), iCareUploadWidget()]

        self.tab_widget.addTab(self.tabs[0], "Add New Template")
        self.tab_widget.addTab(self.tabs[1], "Upload iCare Data")

        self.layout.addWidget(self.tab_widget)
        self.setLayout(self.layout)


class iCareNewTemplateWidget(QWidget):
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
        self.label1 = QLabel("New Template Name:")
        self.iCare_template_name = QLineEdit(self)
        self.file_upload_label = QLabel("No File Chosen")

        self.upload1 = QPushButton("Select Template")
        self.upload1.clicked.connect(self.file_select)
        self.submit1 = QPushButton("Submit New Template")
        self.submit1.clicked.connect(self.submit_new_iCare_template)

        # add widgets
        self.layout.addWidget(self.label1, 0, 0)
        self.layout.addWidget(self.iCare_template_name, 0, 1)
        self.layout.addWidget(self.upload1, 1, 0)
        self.layout.addWidget(self.file_upload_label)
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
    def submit_new_iCare_template(self):
        template_name = self.iCare_template_name.text()
        if (not template_name):
            prompt_error("Please give a Template name")
            return
        if (not self.filepaths):
            prompt_error("Please select a Template file")
            return

        pyxl.add_new_template(template_name, self.filepaths[0])
        prompt_information("New template: '{}' has been added"
                            .format(template_name))

        self.iCare_template_name.setText("")
        self.filepaths = []

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

