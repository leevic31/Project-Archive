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
import db
from gui_helper import (
    prompt_error,
    prompt_information
    )

def get_file_name(path : str) -> str:
    return path[path.rfind("/") + 1:]

class teqWidget(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QGridLayout(self)

#        self.tabs = [iCareNewTemplateWidget(), iCareUploadWidget()]

#        self.tab_widget.addTab(self.tabs[0], "Add New Template")
#        self.tab_widget.addTab(self.tabs[1], "Upload iCare Data")

        # Initialize tab screen
        self.tabs = [iCareNewQueryWidget()]
        self.tab_names = ["Add New Template"]
        self.tab_widget = QTabWidget()

        for i in range(len(self.tabs)):
            self.tab_widget.addTab(self.tabs[i], self.tab_names[i])

        self.layout.addWidget(self.tab_widget)
        self.setLayout(self.layout)

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
        dict_values = db.execute_query_result(query)
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

        self.table1 = QTableWidget()

        # add widgets
        self.layout.addWidget(self.label1, 0, 0)
        self.layout.addWidget(self.iCare_template_name, 0, 1)
        self.layout.addWidget(self.upload1, 1, 0)
        self.layout.addWidget(self.file_upload_label)
        self.layout.addWidget(self.table1, 2, 1)
        self.layout.addWidget(self.submit1, 3, 0)
        self.setLayout(self.layout)

    @pyqtSlot()
    def file_select(self):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.AnyFile)
        dialog.setNameFilter("xlsx (*.xlsx)")

        if dialog.exec_():
            self.filepaths = dialog.selectedFiles()
            file_path = self.filepaths[0]
            self.file_upload_label.setText(get_file_name(file_path))

            columns = pyxl.iCare_parse_columns(file_path)
            self.populateTable(columns)

    def populateTable(self, columns):
        for col in columns:
            print(col)

        self.table1.clearContents()

        self.table1.setColumnCount(2)
        self.table1.setRowCount(len(columns) + 1)
        self.table1.setHorizontalHeaderItem(0, QTableWidgetItem("Column Name"))
        self.table1.setHorizontalHeaderItem(1, QTableWidgetItem("Data Type"))

        for i in range(0, len(columns)):
            self.table1.setItem(i, 0, QTableWidgetItem(columns[i-1]))
            self.table1.setItem(i, 1, QTableWidgetItem("varchar(255)"))

    def aggregateTableData(self):
        columnNames = []
        columnTypes = []
        for i in range(self.table1.rowCount):
            nameItem = self.table1.item(i, 0)
            typeItem = self.table1.item(i, 1)
            columnNames.append(nameItem.text())
            columnTypes.append(typeItem.text())

        return columnNames, columnTypes

    @pyqtSlot()
    def submit_new_iCare_template(self):
        template_name = self.iCare_template_name.text()
        if (not template_name):
            prompt_error("Please give a Template name")
            return
        if (not self.filepaths):
            prompt_error("Please select a Template file")
            return

        columnNames, columnTypes = self.aggregateTableData()

        db.add_new_template(template_name, columnNames, columnTypes)
        prompt_information("New template: '{}' has been added"
                            .format(template_name))

        self.iCare_template_name.setText("")
        self.filepaths = []
