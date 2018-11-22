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

import sys

import database
import exportCSV
import exportPDF
import query
import gui_helper
import presetquery

class ModifyPresetQueryWidget(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()
        self._setup_widget()

    def _setup_widget(self):
        self.query = QTextEdit(self)
        self.descrip = QTextEdit(self)
        self.label = QLabel("Query:")
        self.label2 = QLabel("Description:")
        self.modify_options = {
            "remove",
            "edit"
            }
        self.modify_combobox = QComboBox()
        
        self.cb = QComboBox()
        self.modify2 = QPushButton("Add Preset")
        self.modify2.clicked.connect(self.addpresetclicked)
        for key in self.modify_options:
            self.modify_combobox.addItem(key)
        self.modify = QPushButton("Edit/Remove Preset")
        self.modify.clicked.connect(self.editorremoveclicked)
        
        self.preset_queries = database.get_preset_queries()
        for _id, query, desc in self.preset_queries:
            self.cb.addItem(str(_id)+", "+str(query)+", "+str(desc))
        
        self.layout = QGridLayout(self)
        self.layout.setColumnStretch(0, 2)
        
        self.layout.addWidget(self.label, 0, 0)
        self.layout.addWidget(self.label2, 0 ,1)
        self.layout.addWidget(self.query, 1, 0)
        self.layout.addWidget(self.descrip, 1, 1)
        self.label3 = QLabel("Select Preset to edit/remove")
        self.label4 = QLabel("Add or Edit uses Query, Description inputs")
        self.layout.addWidget(self.label3, 2, 0)
        self.layout.addWidget(self.label4, 2, 1)
        self.layout.addWidget(self.modify_combobox, 3, 0)
        self.layout.addWidget(self.modify2, 3, 1)
        self.layout.addWidget(self.modify, 4, 1)
        self.layout.addWidget(self.cb, 4, 0)

        self.setLayout(self.layout)
        
    def addpresetclicked(self):
        if ((str(self.query.toPlainText()) != "") and (str(self.descrip.toPlainText())) != ""):
            conn = database.get_db_connection()
            presetquery.write_preset(conn, str(self.query.toPlainText()), str(self.descrip.toPlainText()))
            gui_helper.prompt_information("query added successfully")
            conn.close()
        else:
            gui_helper.prompt_error("Please enter a query and description")
    
    def editorremoveclicked(self):
        if (str(self.modify_combobox.currentText()) == "edit"):
            if ((str(self.query.toPlainText()) != "") and (str(self.descrip.toPlainText())) != ""):
                conn = database.get_db_connection()
                editid = str(self.cb.currentText())[:1]
                print(editid)
                presetquery.edit_preset(conn, editid, str(self.query.toPlainText()), str(self.descrip.toPlainText()))
                gui_helper.prompt_information("query edited successfully")
                conn.close()
            else:
                gui_helper.prompt_error("Please enter a query and description")
        elif (str(self.modify_combobox.currentText()) == "remove"):
            conn = database.get_db_connection()
            editid = str(self.cb.currentText())[:1]
            presetquery.remove_preset(conn, editid)
            conn.close()
            gui_helper.prompt_information("query removed successfully")
        else:
             gui_helper.prompt_error("if you got this that's bad")


if (__name__ == "__main__"):
    app = QApplication(sys.argv)
    ex = ModifyPresetQueryWidget()
    ex.show()
    sys.exit(app.exec_())
