'''Program for smag'''
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
 
class App(QMainWindow):
 
	def __init__(self):
		super().__init__()
		self.title = 'SMAG'
		self.left = 20
		self.top = 35
		self.width = 640
		self.height = 480
		self.initUI()
 
	def initUI(self):
		self.setWindowTitle(self.title)
		self.setGeometry(self.left, self.top, self.width, self.height)
		self.textbox = QLineEdit(self)
		self.textbox.move(20, 40)
		self.textbox.resize(280,40)
		button = QPushButton('Click here', self)
		button.setToolTip('This is an example button')
		button.move(100,90)
		button.clicked.connect(self.on_click)
		self.statusBar().showMessage('Idle')
		mainMenu = self.menuBar() 
		fileMenu = mainMenu.addMenu('File')
		editMenu = mainMenu.addMenu('Edit')
		viewMenu = mainMenu.addMenu('View')
		searchMenu = mainMenu.addMenu('Search')
		toolsMenu = mainMenu.addMenu('Tools')
		helpMenu = mainMenu.addMenu('Help')
 
		exitButton = QAction(QIcon('exit24.png'), 'Exit', self)
		exitButton.setShortcut('Ctrl+Q')
		exitButton.setStatusTip('Exit application')
		exitButton.triggered.connect(self.close)
		fileMenu.addAction(exitButton)
		self.show()

	@pyqtSlot()
	def on_click(self):
		textboxValue = self.textbox.text()
		QMessageBox.question(self, 'Message - SMAG', "You typed: " + textboxValue, QMessageBox.Ok, QMessageBox.Ok)
		self.textbox.setText("")
 
if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = App()
	sys.exit(app.exec_())