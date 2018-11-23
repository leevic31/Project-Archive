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
    QTabWidget,
    QTableWidget,
    QTableWidgetItem,
    QTextEdit,
    QVBoxLayout,
    QListWidget,
    QWidget
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

class iCareNewQueryWidget(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()
        self._setup_widget()

    def _setup_widget(self):
        self.reportgraphs = list()
		
        self.query = QTextEdit(self)
        self.label1 = QLabel("Query:")
        self.label2 = QLabel("Output:")

        self.label3 = QLabel("In Report:")
        self.reportitems = QListWidget()
        self.addtoreport = QPushButton("Add Graph to Report")
        self.addtoreport.clicked.connect(self.add_graph)

        self.submit1 = QPushButton("Execute Query")
        self.submit1.clicked.connect(self.run_query)

        self.export1 = QPushButton("Export Data")
        self.export1.clicked.connect(self.export_data)

        self._setup_export_combobox()

        self.table1 = QTableWidget()

        self.export_graph_options = {
                "bar",
                "line",
                "pie"
                }
        self.export_combobox2 = QComboBox()
        for key in self.export_graph_options:
            self.export_combobox2.addItem(key)

        # set layouts
        self.layout = QGridLayout(self)
        self.layout.setColumnStretch(0, 3)

        # add "Query" label
        self.layout.addWidget(self.label1, 0, 0)
        # add query textbox
        self.layout.addWidget(self.query, 1, 0)
        # add "Execute Query" button
        self.layout.addWidget(self.submit1, 1, 1)
        # add "Output" label
        self.layout.addWidget(self.label2, 2, 0)
        # add file option combobox
        self.layout.addWidget(self.export_combobox, 2, 1)
        # add query output result table
        self.layout.addWidget(self.table1, 3, 0)
        # add graph option combobox
        self.layout.addWidget(self.export_combobox2, 3, 1)
        # add "Export Data" button
        self.setLayout(self.layout)
        
        self.layout.addWidget(self.label3, 4, 0)
        self.layout.addWidget(self.addtoreport, 4, 1)
        self.layout.addWidget(self.reportitems, 5, 0)
        self.layout.addWidget(self.export1, 5, 1)

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
        """
        query_text = self.query.toPlainText()
        if (len(query_text) == 0):
            gui_helper.prompt_error("Please enter a query")
            return

        export_option = self.export_options[self.export_combobox.currentText()]
        filepath = gui_helper.prompt_file_save()

        try:
            export_option.export(filepath, query_text)
            gui_helper.prompt_information("Data has been succesfully exported!")
        except Exception as e:
            gui_helper.prompt_error("Failed to export data: " + repr(e))
        """
        with PdfPages('reportpdf.pdf') as pdf:
            conn = database.get_db_connection()
            for x in self.reportgraphs:
                dict_values = query.manual_sql_query(conn, x[:-3])
                if (x[-3:] == "pie"):
                    plt = graph.pie_chart("pie", dict_values)
                if (x[-3:] == "bar"):
                    plt = graph.bar_chart("bar", dict_values)
                if (x[-3:] == "lin"):
                    plt = graph.line_chart("line", dict_values)
                fig = plt.gcf()
                pdf.savefig()
                plt.close(fig)
            conn.close()
            
    def add_graph(self):
        graphtype = str(self.export_combobox2.currentText())
        queryval = str(self.query.toPlainText())
        
        if (queryval == ""):
            gui_helper.prompt_error("Please input a query")
            return
        if (graphtype == "pie"):
            self.reportitems.addItem(queryval)
            queryval = queryval + "pie"
        elif (graphtype == "bar"):
            self.reportitems.addItem(queryval)
            queryval = queryval + "bar"
        elif (graphtype == "line"): 
            self.reportitems.addItem(queryval)
            queryval = queryval + "lin"
        self.reportgraphs.append(queryval)

if (__name__ == "__main__"):
    app = QApplication(sys.argv)
    ex = iCareNewQueryWidget()
    ex.show()
    sys.exit(app.exec_())
