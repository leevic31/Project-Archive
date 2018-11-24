from PyQt5.QtWidgets import (
    QAction,
    QApplication,
    QButtonGroup,
    QComboBox,
    QDialog,
    QFileDialog,
    QGridLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QRadioButton,
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
import gui_helper
import presetquery

_PRESET_WIDGET_POS = (4, 0)

class ModifyPresetQueryWidget(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()
        self._setup_widget()

    def _setup_widget(self):
        self.addRadioBtn = QRadioButton("Add a Preset Query")
        self.editRadioBtn = QRadioButton("Edit a Preset Query")
        self.removeRadioBtn = QRadioButton("Remove a Preset Query")
        self.addRadioBtn.setChecked(True)

        self.addRadioBtn.toggled.connect(self.setUIToAddPreset)
        self.editRadioBtn.toggled.connect(self.setUIToEditPreset)
        self.removeRadioBtn.toggled.connect(self.setUIToRemovePreset)

        self.currentWidget = AddPresetQueryWidget()

        self.buttonGroup = QButtonGroup()
        self.buttonGroup.addButton(self.addRadioBtn)
        self.buttonGroup.addButton(self.editRadioBtn)
        self.buttonGroup.addButton(self.removeRadioBtn)

        self.layout = QGridLayout(self)
        self.layout.setColumnStretch(0, 2)

        self.layout.addWidget(self.addRadioBtn, 0, 0)
        self.layout.addWidget(self.editRadioBtn, 1, 0)
        self.layout.addWidget(self.removeRadioBtn, 2, 0)
        self.reloadPresetQueryUI()

        self.setLayout(self.layout)

    def reloadPresetQueryUI(self):
        self.layout.addWidget(self.currentWidget,
                _PRESET_WIDGET_POS[0], _PRESET_WIDGET_POS[1])

    @pyqtSlot()
    def setUIToAddPreset(self):
        if (self.addRadioBtn.isChecked()):
            self.layout.removeWidget(self.currentWidget)
            self.currentWidget.deleteLater()
            self.currentWidget = AddPresetQueryWidget()
            self.reloadPresetQueryUI()

    @pyqtSlot()
    def setUIToEditPreset(self):
        if (self.editRadioBtn.isChecked()):
            self.layout.removeWidget(self.currentWidget)
            self.currentWidget.deleteLater()
            self.currentWidget = EditQueryWidget()
            self.reloadPresetQueryUI()

    @pyqtSlot()
    def setUIToRemovePreset(self):
        if (self.removeRadioBtn.isChecked()):
            self.layout.removeWidget(self.currentWidget)
            self.currentWidget.deleteLater()
            self.currentWidget = RemoveQueryWidget()
            self.reloadPresetQueryUI()

class AddPresetQueryWidget(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()
        self._setup_widget()

    def _setup_widget(self):
        self.query = QTextEdit(self)
        self.description = QTextEdit(self)
        self.label = QLabel("Query:")
        self.label2 = QLabel("Description:")

        self.submit = QPushButton("Add Preset")
        self.submit.clicked.connect(self.addpresetclicked)

        self.layout = QGridLayout(self)
        self.layout.setColumnStretch(0, 2)

        self.layout.addWidget(self.label, 0, 0)
        self.layout.addWidget(self.label2, 0 ,1)
        self.layout.addWidget(self.query, 1, 0)
        self.layout.addWidget(self.description, 1, 1)
        self.layout.addWidget(self.submit, 2, 1)

        self.setLayout(self.layout)

    @pyqtSlot()
    def addpresetclicked(self):
        query_text = self.query.toPlainText()
        description_text = self.description.toPlainText()
        if (not query_text or not description_text):
            gui_helper.prompt_error("Please enter a query and description")
            return

        try:
            presetquery.write_preset(query_text, description_text)
            gui_helper.prompt_information("query added successfully")
        except Exception as e:
            gui_helper.prompt_error("Failed to add preset query: " + repr(e))


class EditQueryWidget(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()
        self._setup_widget()

    def _setup_widget(self):
        self.query = QTextEdit(self)
        self.description = QTextEdit(self)

        self.submit = QPushButton("Save Preset")
        self.submit.clicked.connect(self.editClicked)

        self.cb = QComboBox()
        self._populate_preset_combobox()

        self.cb.currentTextChanged.connect(self.populateTextBoxes)

        self.label = QLabel("Select Preset to edit")
        self.label2 = QLabel("Query:")
        self.label3 = QLabel("Description:")

        self.layout = QGridLayout(self)

        self.layout.addWidget(self.label, 0, 0)
        self.layout.addWidget(self.cb, 1, 0)
        self.layout.addWidget(self.label2, 2, 0)
        self.layout.addWidget(self.query, 3, 0)
        self.layout.addWidget(self.label3, 4, 0)
        self.layout.addWidget(self.description, 5, 0)
        self.layout.addWidget(self.submit, 5, 1)

        self.setLayout(self.layout)
        self.populateTextBoxes()

    def _populate_preset_combobox(self):
        self.cb.clear()
        self.preset_queries = database.get_preset_queries()
        for _id, query, desc in self.preset_queries:
            self.cb.addItem("{}; {}".format(query, desc))

    @pyqtSlot()
    def editClicked(self):
        query_text = self.query.toPlainText()
        description_text = self.description.toPlainText()
        if (not query_text or not description_text):
            gui_helper.prompt_error("Please enter a query and description")
            return

        try:
            index = self.cb.currentIndex()
            editid = self.preset_queries[index][0]

            presetquery.edit_preset(editid, self.query.toPlainText(), self.description.toPlainText())
            gui_helper.prompt_information("query edited successfully")
            self._populate_preset_combobox()
        except Exception as e:
            gui_helper.prompt_error("Failed to edit preset query: " + repr(e))

    @pyqtSlot()
    def populateTextBoxes(self):
        index = self.cb.currentIndex()
        if (index >= 0):
            query_text = self.preset_queries[index][1]
            description_text = self.preset_queries[index][2]

            self.query.setText(query_text)
            self.description.setText(description_text)

class RemoveQueryWidget(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()
        self._setup_widget()

    def _setup_widget(self):
        self.submit = QPushButton("Remove Preset")
        self.submit.clicked.connect(self.removeClicked)

        self.cb = QComboBox()
        self._populate_preset_combobox()

        self.label = QLabel("Select Preset to remove")

        self.layout = QGridLayout(self)
        self.layout.setColumnStretch(0, 2)

        self.layout.addWidget(self.label, 0, 0)
        self.layout.addWidget(self.cb, 0, 1)
        self.layout.addWidget(self.submit, 1, 1)

        self.setLayout(self.layout)

    def _populate_preset_combobox(self):
        self.cb.clear()
        self.preset_queries = database.get_preset_queries()
        for _id, query, desc in self.preset_queries:
            self.cb.addItem("{}; {}".format(query, desc))

    @pyqtSlot()
    def removeClicked(self):
        try:
            index = self.cb.currentIndex()
            editid = self.preset_queries[index][0]

            presetquery.remove_preset(editid)

            gui_helper.prompt_information("query removed successfully")
            self._populate_preset_combobox()
        except Exception as e:
            gui_helper.prompt_error("Failed to remove preset query: " + repr(e))

if (__name__ == "__main__"):
    app = QApplication(sys.argv)
    ex = ModifyPresetQueryWidget()
    ex.show()
    sys.exit(app.exec_())
