from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QLabel, QLineEdit, QVBoxLayout
import pytest

defaultLabelText = "orca"

class MainWindow(QMainWindow):
	def __init__(self, name = "My App", buttonText = "Click Me!", x = 1000, y = 1000):
		super().__init__()
		
		self.buttonIsChecked = True

		self.label = QLabel()
		self.label.setText(defaultLabelText)
		self.input = QLineEdit()
		#self.input.textChanged.connect(self.label.setText)
		
		self.setWindowTitle(name);
		self.button = QPushButton(buttonText)
		#self.button.setFixedSize(QSize(500,100))
		#self.button.setCheckable(True)
		#self.button.clicked.connect(self.theButtonWasClicked)
		#self.button.setChecked(self.buttonIsChecked)

		#self.windowTitleChanged.connect(self.theWindowTitleChanged)		

		layout = QVBoxLayout()

		layout.addWidget(self.input)
		layout.addWidget(self.button)
		layout.addWidget(self.label)

		container = QWidget()
		container.setLayout(layout)

		self.setFixedSize(QSize(x, y))
		self.setCentralWidget(container)	
	
	def theButtonWasClicked(self):
		item = self.input.text()
		#self.label.setText(text)
		displayAisleOfItem(self, entryList, item)
		#self.button.setText("You already clicked me moron.")

	def theWindowTitleChanged(self):
		print("title has changed")	
	


def printNumList(window, numList):
	numList.sort()
	currentNumber = window.label.text()	
	if currentNumber == defaultLabelText:
		currentNumber = None
	
	elif int(currentNumber) == numList[(len(numList) - 1)]:
		currentNumber = None		

	if currentNumber == None:
		window.label.setText(str(numList[0]))
		return
		
	
	
	for x in range(len(numList)):
		if int(numList[x]) == int(currentNumber):
			window.label.setText(str(numList[x+1]))

		

#testDictionaryEntryList(entryList)

#printAvailableItems(entryList)

app = QApplication([])

#window = QWidget()
#window = QPushButton("Click Me")
window = MainWindow("Number iterator", "iterate")

numList = [1, 2, 3, 5, 4]

window.button.clicked.connect(lambda: printNumList(window, numList))

window.show()

app.exec()

