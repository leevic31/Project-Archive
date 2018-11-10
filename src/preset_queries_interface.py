import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QComboBox,
    QPushButton,
    QMessageBox,
    QRadioButton
    )
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class presetQueriesInterface(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()
        
        layout = QHBoxLayout()
        self.cb = QComboBox()
        # TODO: ANDREI connect to preset quries api to add to drop down menu
        #current text method 
        self.cb.addItem("option1")
        self.cb.addItem("option2")
        
        layout.addWidget(self.cb)
        self.setLayout(layout)
        self.setWindowTitle("Preset Queries")
        
        # create button to generate the selected query
        self.button = QPushButton("Generate", self)
        self.button.move(600, 500)
        
        # connect button to function on_click
        #TODO: generate report when click
        #self.button.clicked.connect(self.on_click)
        self.setWindowModality(Qt.ApplicationModal)
        #self.exec_()
        
        self.b1 = QRadioButton("CSV")
        self.b1.setChecked(True)
        #self.b1.toggled.connect(lambda:self.btnstate(self.b1))
        layout.addWidget(self.b1)
        
        self.b2 = QRadioButton("PDF")
        #self.b2.toggled.connect(lambda:self.btnstate(self.b2))
        layout.addWidget(self.b2)
        
        self.setLayout(layout)
    
    #@pyqtSlot()
    #def on_click(self):
        # if CSV
        #if b1.isChecked() == True:
            # export to CSV
        # else if PDF
        #else if b2.isChecked() == True:
            # export to PDF

        
def main():
    app = QApplication(sys.argv)
    ex = presetQueriesInterface()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()