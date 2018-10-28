from PyQt5.QtWidgets import QMessageBox

from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

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
