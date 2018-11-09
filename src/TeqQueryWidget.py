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
        if (not query.endswith(";")):
            query = query + ";"

        print("Query:", query)
        dict_values = database.execute_query_result(query)
        self.populateTable(dict_values)
        print(dict_values)

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
        pass

