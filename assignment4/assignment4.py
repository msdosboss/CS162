from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QLabel, QLineEdit, QVBoxLayout
import pytest

class entry:
	def __init__(self, name, row):
		self.name = name
		self.row = row

def dictionaryEntryList(entryList):
	dict = {}
	for entry in entryList:
		dict[entry.name.lower()] = entry.row
	return dict

def testDictionaryEntryList():
	localEntryList = []

	localEntryList.append(entry("Milk", 4))
	localEntryList.append(entry("Yogurt", 4))
	localEntryList.append(entry("Chicken Nuggets", 5))
	localEntryList.append(entry("Apple", 6))
	localEntryList.append(entry("Banana", 6))
	localEntryList.append(entry("Chicken", 7))

	dict = dictionaryEntryList(localEntryList)
	for entryy in localEntryList:
		assert dict[entryy.name.lower()] == entryy.row


def displayAisleOfItem(window, entryList, item):
	#window.label.setText(entryList[0].name)
	dict = dictionaryEntryList(entryList)
	item = item.lower()
	if(item in dict):
		window.label.setText(f"{item} is in row {dict[item]}")
	else:
		window.label.setText(f"{item} is not in the database")

class MainWindow(QMainWindow):
	def __init__(self, name = "My App", buttonText = "Click Me!", x = 1000, y = 1000):
		super().__init__()
		
		self.buttonIsChecked = True

		self.label = QLabel()

		self.input = QLineEdit()
		#self.input.textChanged.connect(self.label.setText)
		
		self.setWindowTitle(name);
		self.button = QPushButton(buttonText)
		#self.button.setFixedSize(QSize(500,100))
		#self.button.setCheckable(True)
		self.button.clicked.connect(self.theButtonWasClicked)
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

def printAvailableItems(entryList):
	for x in range(len(entryList)):
		print(f"{entryList[x].name} is located in row {entryList[x].row}")

def printAvailableItemsGui(root, entryList):	#not working in pyQT yet
	for x in entryList:
		continue

entryList = []

entryList.append(entry("Milk", 4))
entryList.append(entry("Yogurt", 4))
entryList.append(entry("Chicken Nuggets", 5))
entryList.append(entry("Apple", 6))
entryList.append(entry("Banana", 6))
entryList.append(entry("Chicken", 7))

#testDictionaryEntryList(entryList)

#printAvailableItems(entryList)

app = QApplication([])

#window = QWidget()
#window = QPushButton("Click Me")
window = MainWindow("Grocery App", "Submit")

window.show()

app.exec()

