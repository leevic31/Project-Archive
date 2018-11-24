from PyQt5.QtWidgets import (
    QAction,
    QApplication,
    QComboBox,
    QGridLayout,
    QHeaderView,
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
    QListWidget,
    QWidget,
    )

from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot, Qt

import sys

import database
import exportCSV
import exportPDF
import query
import gui_helper
import graph
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

class TeqCustomQueryWidget(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()
        self._setup_widget()

    def _setup_widget(self):
        self.query = QTextEdit(self)

        self.submit1 = QPushButton("Execute Query")
        self.submit1.clicked.connect(self.run_query)

        self.export1 = QPushButton("Export Data")
        self.export1.clicked.connect(self.export_data)

        self._setup_export_combobox()
        self.table1 = QTableWidget()

        # set layouts
        self.layout = QGridLayout(self)
        self.layout.setColumnStretch(0, 3)

        # add "Query" label
        self.layout.addWidget(QLabel("Query:"), 0, 0)
        # add query textbox
        self.layout.addWidget(self.query, 1, 0)
        # add "Execute Query" button
        self.layout.addWidget(self.submit1, 1, 1)
        # add "Output" label
        self.layout.addWidget(QLabel("Query Output:"), 2, 0)
        # add file option combobox
        self.layout.addWidget(self.export_combobox, 2, 1)
        # add query output result table
        self.layout.addWidget(self.table1, 3, 0)
        self.layout.addWidget(self.export1, 3, 1)

        self.setLayout(self.layout)

    def _setup_export_combobox(self):
        self.export_options = {
                "csv": exportCSV.ExportCSV(),
                "pdf": exportPDF.ExportPDF()
                }
        self.export_combobox = QComboBox()
        for key in self.export_options:
            self.export_combobox.addItem(key)

    @pyqtSlot()
    def run_query(self):
        query = self.query.toPlainText()
        if (len(query) == 0):
            gui_helper.prompt_error("Please enter a query")
            return
        try:
            dict_values = database.execute_query_result(query)
            if (dict_values):
                self.populateTable(dict_values)
            gui_helper.prompt_information("query executed successfully")
        except Exception as e:
            gui_helper.prompt_error("Failed to run Query: " + repr(e))

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
            gui_helper.prompt_error("Please enter a query")
            return

        export_option = self.export_options[self.export_combobox.currentText()]
        filepath = gui_helper.prompt_file_save()
        if (not file_path):
            return

        try:
            export_option.export(filepath, query_text)
            gui_helper.prompt_information("Data has been succesfully exported!")
        except Exception as e:
            gui_helper.prompt_error("Failed to export data: " + repr(e))

        with PdfPages(filepath) as pdf:
            conn = database.get_db_connection()
            for i in range(self.report_table.rowCount()):
                query_text = self.report_table.item(i, 1).text()
                graph_type = self.report_table.item(i, 0).text()

                dict_values = query.manual_sql_query(conn, query_text)
                try:
                    plt = self.export_graph_options[graph_type](graph_type, dict_values)

                    fig = plt.gcf()
                    pdf.savefig()
                    plt.close(fig)
                except Exception as e:
                    gui_helper.prompt_error("Failed to export graph {}: ".format(i) + repr(e))
            conn.close()

    @pyqtSlot()
    def add_graph(self):
        graph_type = self.export_combobox.currentText()
        query_text = self.query.toPlainText()
        
        if (len(query_text) == 0):
            gui_helper.prompt_error("Please enter a query")
            return

        row_count = self.report_table.rowCount()
        self.report_table.insertRow(row_count)
        self.report_table.setItem(row_count, 0, QTableWidgetItem(graph_type))
        self.report_table.setItem(row_count, 1, QTableWidgetItem(query_text))

class TeqGraphGenerationWidget(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()
        self._setup_widget()

    def _setup_widget(self):
        self.query = QTextEdit(self)

        self.addtoreport = QPushButton("Add Graph to Report")
        self.addtoreport.clicked.connect(self.add_graph)

        self.submit1 = QPushButton("Execute Query")
        self.submit1.clicked.connect(self.run_query)

        self.export1 = QPushButton("Export Graphs")
        self.export1.clicked.connect(self.export_data)

        self.clear1 = QPushButton("Clear Graphs")
        self.clear1.clicked.connect(self.clear_graphs)

        self._setup_graph_export_combobox()
        self._setup_report_queue_table()

        self.table1 = QTableWidget()

        # set layouts
        self.layout = QGridLayout(self)
        self.layout.setColumnStretch(0, 3)

        self.layout.addWidget(QLabel("Query:"), 0, 0)
        # add query textbox
        self.layout.addWidget(self.query, 1, 0)
        self.layout.addWidget(self.submit1, 1, 1)

        self.layout.addWidget(QLabel("In Current Report:"), 2, 0)
        # add file option combobox
        self.layout.addWidget(self.export_combobox, 2, 1)
        # add query output result table

        self.layout.addWidget(self.report_table, 3, 0)
        self.layout.addWidget(self.addtoreport, 3, 1)

        self.layout.addWidget(QLabel("Query Output:"), 4, 0)
        self.layout.addWidget(self.clear1, 4, 1)

        self.layout.addWidget(self.table1, 5, 0)
        self.layout.addWidget(self.export1, 5, 1)

        self.setLayout(self.layout)

    def _setup_graph_export_combobox(self):
        self.export_graph_options = {
                "bar": graph.bar_chart,
                "line": graph.line_chart,
                "pie": graph.pie_chart
                }
        self.export_combobox = QComboBox()
        for key in self.export_graph_options:
            self.export_combobox.addItem(key)

    def _setup_report_queue_table(self):
        self.report_table = QTableWidget()
        self.report_table.setColumnCount(2)
        header = self.report_table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        self.report_table.setHorizontalHeaderItem(0, QTableWidgetItem("Graph Type"))
        self.report_table.setHorizontalHeaderItem(1, QTableWidgetItem("Query"))

    @pyqtSlot()
    def run_query(self):
        query = self.query.toPlainText()
        if (len(query) == 0):
            gui_helper.prompt_error("Please enter a query")
            return
        try:
            dict_values = database.execute_query_result(query)
            if (dict_values):
                self.populateTable(dict_values)
            gui_helper.prompt_information("query executed successfully")
        except Exception as e:
            gui_helper.prompt_error("Failed to run Query: " + repr(e))

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
    def add_graph(self):
        graph_type = self.export_combobox.currentText()
        query_text = self.query.toPlainText()
        
        if (len(query_text) == 0):
            gui_helper.prompt_error("Please enter a query")
            return

        row_count = self.report_table.rowCount()
        self.report_table.insertRow(row_count)
        self.report_table.setItem(row_count, 0, QTableWidgetItem(graph_type))
        self.report_table.setItem(row_count, 1, QTableWidgetItem(query_text))

    @pyqtSlot()
    def clear_graphs(self):
        self.report_table.setRowCount(0)

    @pyqtSlot()
    def export_data(self):
        query_text = self.query.toPlainText()
        if (len(query_text) == 0):
            gui_helper.prompt_error("Please enter a query")
            return

        file_path = gui_helper.prompt_file_save()

        if (not file_path):
            return

        with PdfPages(file_path) as pdf:
            conn = database.get_db_connection()
            for i in range(self.report_table.rowCount()):
                query_text = self.report_table.item(i, 1).text()
                graph_type = self.report_table.item(i, 0).text()

                dict_values = query.manual_sql_query(conn, query_text)
                try:
                    plt = self.export_graph_options[graph_type](graph_type, dict_values)

                    fig = plt.gcf()
                    pdf.savefig()
                    plt.close(fig)
                except Exception as e:
                    gui_helper.prompt_error("Failed to export graph {}: ".format(i) + repr(e))
            conn.close()
            gui_helper.prompt_information("Graphs has been successfully exported")

if (__name__ == "__main__"):
    app = QApplication(sys.argv)
    ex = iCareNewQueryWidget()
    ex.show()
    sys.exit(app.exec_())
