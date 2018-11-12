import sys
import query
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QToolTip 
from PyQt5.QtWidgets import QMessageBox, QStatusBar, QLineEdit, QMenuBar, QAction
from PyQt5.QtCore import QCoreApplication

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.title = "SQL Query"
        self.left = 100
        self.top = 100
        self.width = 680
        self.height = 540
        
        self.ebutton = QPushButton("<-", self)
        self.ebutton.setToolTip("Close the window")
        self.ebutton.resize(30, 30)
        self.ebutton.clicked.connect(self.CloseApp)
        
        self.query = QLineEdit(self)
        self.query.move(200, 200)
        self.query.resize(280,40)
        self.queryButton = QPushButton("Submit Query", self)
        self.queryButton.move(290, 250)
        self.queryButton.clicked.connect(self.SubmitQuery)
        
     
     
        self.menubar = QMenuBar()
        self.setMenuBar(self.menubar)
        mainMenu = self.menubar.addMenu("Options")
        
        
        self.InitUI();
        
    def InitUI(self):
        self.statusBar().showMessage("Please input sql query")
        
        
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()
        
    def CloseApp(self):
        reply = QMessageBox.question(self, "Exit Query?", "Are you sure you want to go back?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.close()
            
    def SubmitQuery(self):
        textValue = self.query.text()   # on click gives typed in value
		#########################################################
		# 	INSERT METHOD HERE TO USE textValue FOR QUERY		#
		#########################################################
        genReport = QMessageBox.question(self, "Generate Report?",
                                      "Generate Report using query '" + textValue + "'", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if genReport == QMessageBox.Yes:
             self.close()	            #!!!!!!!!!! remove this line after adding generate report
			#######################
			#	GENERATE REPORT
			#######################
	
App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
