from PyQt5.QtWidgets import QMessageBox, QFileDialog

from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

def prompt_error(message, title="Error"):
    '''Prompts an error message to the user'''
    messagebox = QMessageBox()
    messagebox.setIcon(QMessageBox.Critical)
    messagebox.setText(message)
    messagebox.setStandardButtons(QMessageBox.Close)
    messagebox.setWindowTitle(title)
    messagebox.setWindowModality(Qt.ApplicationModal)
    messagebox.exec_()

def prompt_information(message, title="Notice"):
    '''Prompts an information message to the user'''
    messagebox = QMessageBox()
    messagebox.setIcon(QMessageBox.Information)
    messagebox.setText(message)
    messagebox.setStandardButtons(QMessageBox.Close)
    messagebox.setWindowTitle(title)
    messagebox.setWindowModality(Qt.ApplicationModal)
    messagebox.exec_()

def prompt_file_chooser():
    dialog = QFileDialog()
    dialog.setFileMode(QFileDialog.ExistingFiles)
    dialog.setNameFilter("xlsx (*.xlsx)")

    if dialog.exec_():
        return dialog.selectedFiles()
    return []

def prompt_file_save():
    dialog = QFileDialog()
    dialog.setFileMode(QFileDialog.AnyFile)
    if dialog.exec_():
        filepaths = dialog.selectedFiles()
        if (filepaths):
            return filepaths[0]

    return None
