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

import pyxl
import database
import exportFile
import query
import gui_helper

from gui_helper import (
    prompt_error,
    prompt_information
    )

class iCareNewQueryWidget(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()
        self._setup_widget()

    def _setup_widget(self):
        self.query = QTextEdit(self)
        self.label1 = QLabel("Query:")
        self.label2 = QLabel("Output:")
        self.submit1 = QPushButton("Execute Query")
        self.submit1.clicked.connect(self.run_query)
        self.export1 = QPushButton("Export Data")
        self.export1.clicked.connect(self.export_data)

        self.table1 = QTableWidget()

        # set layouts
        self.layout = QGridLayout(self)
        self.layout.setColumnStretch(0, 3)

        # add widgets
        self.layout.addWidget(self.label1, 0, 0)
        self.layout.addWidget(self.query, 1, 0)
        self.layout.addWidget(self.submit1, 1, 1)
        self.layout.addWidget(self.label2, 2, 0)
        self.layout.addWidget(self.table1, 3, 0)
        self.layout.addWidget(self.export1, 3, 1)
        self.setLayout(self.layout)

    @pyqtSlot()
    def run_query(self):
        query = self.query.toPlainText()
        if (len(query) == 0):
            prompt_error("Please enter a query")
            return
        try:
            dict_values = database.execute_query_result(query)
            if (dict_values):
                self.populateTable(dict_values)
            gui_helper.prompt_information("query executed successfully")
        except Exception as e:
            gui_helper.prompt_error(str(e))

    def populateTable(self, column_values):
        self.table1.clearContents()

        self.table1.setColumnCount(len(column_values))
        for key in column_values:
            self.table1.setRowCount(len(column_values[key]))
            break
        for i, key in enumerate(column_values):
            self.table1.setHorizontalHeaderItem(i, QTableWidgetItem(key))
            col_vals = column_values[key]
            for j, val in enumerate(col_vals):
                self.table1.setItem(j, i, QTableWidgetItem(str(val)))

    @pyqtSlot()
    def export_data(self):
        query_text = self.query.toPlainText()
        if (len(query_text) == 0):
            prompt_error("Please enter a query")
            return

        try:
            conn = database.get_db_connection()
            dataframe = query.manual_sql_query(conn, query_text)
            dialog = QFileDialog()
            dialog.setFileMode(QFileDialog.AnyFile)

            if dialog.exec_():
                filepaths = dialog.selectedFiles()
                self.file_save(filepaths[0], dataframe)
        except Exception as e:
            gui_helper.prompt_error(str(e))


    @pyqtSlot()
    def file_save(self, file_path, dataframe):
        if (exportFile.exportCSV(file_path, dataframe)):
            gui_helper.prompt_information("File has been succesfully saved!")
        else:
            gui_helper.prompt_error("Failed to save file")

