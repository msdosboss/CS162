from PyQt6.QtCore import QSize, Qt, QTimer
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QGridLayout, QTableWidget, QTableWidgetItem
import pytest
import time
import random
import fileio

defaultLabelText = "orca"

#grocList = [['fortnite gift card', 'banana', 'apple'], ['copy of minecraft', 'milk', 'Ninja Funko Pop'], ['ASDFGHJKL:', 'orca', '3rd item']]
grocList = [    #list created by chatgpt
    ['snacks', 'cereal', 'bread'],
    ['dairy', 'eggs', 'cheese'],
    ['frozen foods', 'ice cream', 'pizza'],
    ['produce', 'lettuce', 'tomatoes'],
    ['beverages', 'soda', 'juice'],
    ['canned goods', 'soup', 'beans'],
    ['meat', 'chicken', 'beef'],
    ['condiments', 'ketchup', 'mayonnaise'],
    ['household', 'paper towels', 'dish soap']
]

def listToDict(grocList):
	grocDict = {}
	for outer in range(len(grocList)):
		for inner in range(len(grocList[outer])):
			grocDict[grocList[outer][inner].lower()] = outer + 1	#the key is the groc item and the value is its row. This will allow us to quickly look up what aisle each item is in

	return grocDict	

grocDict = listToDict(grocList)

def listToTwoDList(enteredList, grocDict):
	sortedList = []
	previousAisle = 0
	tempList = []
	for item in enteredList:
		currentAisle = grocDict[item]
		if currentAisle == previousAisle:
			tempList.append(item)
		else:
			if previousAisle != 0:
				sortedList.append(tempList)
			while currentAisle > previousAisle + 1:
				sortedList.append([])
				previousAisle += 1
			tempList = []
			tempList.append(item)
		previousAisle = currentAisle
    
	sortedList.append(tempList)
	return sortedList
            

class SecondWindow(QWidget):
	def __init__(self, x = 1000, y = 1000):
		super().__init__()
		
		#self.setFixedSize(QSize(x, y))
		
		self.layout = QGridLayout()
		
		self.labelWidgets = []
		
		self.input = QLineEdit()
		
		self.sortedList = []

		self.buttonAdd = QPushButton("Add Item")

		self.buttonSort = QPushButton("Sort")

		self.buttonWrite = QPushButton("Write To File")

		self.layout.addWidget(self.input, 0, 0, 1, 4)

		self.layout.addWidget(self.buttonAdd, 0, 4, 1, 3)

		self.layout.addWidget(self.buttonSort, 0, 7, 1, 3)

		self.container = QWidget()

		self.usedItems = []

		self.buttonAdd.clicked.connect(self.verifyEntry)
		self.buttonSort.clicked.connect(self.sortList)

		self.buttonWrite.clicked.connect(self.fileWrite)
		
		self.setGUI()


	def verifyEntry(self):
		orcaFlag = False
		try:
			for aisle in grocList:
				for item in aisle:
					if self.input.text().lower() == item.lower():
						if self.input.text().lower() in self.usedItems:
							raise ValueError("Item already used")
						self.addEntry(self.input.text().lower(), len(self.labelWidgets) + 1, 0, 1, 1)
						self.usedItems.append(self.input.text().lower())
						orcaFlag = True
						break
				if orcaFlag:
					break
			
			if not orcaFlag:
				raise LookupError("Item not in list")
		
		except LookupError as le:
			self.flashBar()
			print(le)
	
		except ValueError as ve:
			self.flashBar()
			print(ve)


		else:
			self.input.setText("")
			self.setGUI()

	def fileWrite(self):
		fileio.outputListToFile(self.sortedList)

	def addEntry(self, val, posy, posx, leny = 1, lenx = 1):
		label = QLabel()
		label.setText(str(val))
		self.labelWidgets.append(label)
		self.layout.addWidget(self.labelWidgets[(len(self.labelWidgets) - 1)], posy, posx, leny, lenx)
		return len(self.labelWidgets) - 1	#return the index of the widget
	
	def setGUI(self):
		self.setLayout(self.layout)

	
	def flashBar(self):
		ogStyle = self.input.styleSheet()
		self.input.setStyleSheet("background-color: red")
		QTimer.singleShot(500, lambda: self.input.setStyleSheet(ogStyle))


	def clearLayout(self):
		while self.layout.count():
			item = self.layout.takeAt(0)
			widget = item.widget()
			if widget is not None:
				widget.deleteLater()
			else:
				#if there is a layout in the layout it will recursivly delete it
				layout = item.layout()
				if layout is not None:
					self.clearLayout(layout)
		self.labelWidgets = []
		self.setGUI()
			
	
	def sortList(self):
		enteredList = []
		for item in self.labelWidgets:	#create list of entered items
			enteredList.append(item.text())
		enteredList = self.mergeSort(enteredList)	#this mergeSort is made for sorting a list of ints. So I use the dict value that corresponds with the item (an int) to sort the list
		self.clearLayout()
		self.layout.addWidget(self.buttonWrite, 0, 0, 1, 10)
		previousAisle = 0
		n = 0
		for item in enteredList:
			currentAisle = grocDict[item]
			if previousAisle == currentAisle:
				self.addEntry(item, currentAisle + 1, n)
				n += 1
			else:
				n = 0
				self.addEntry(f"Aisle {currentAisle}", currentAisle + 1, n)
				n += 1
				self.addEntry(item, currentAisle + 1, n)
				n += 1
				
			previousAisle = currentAisle
		self.setGUI()
		sortedList = listToTwoDList(enteredList, grocDict)
		self.sortedList = sortedList

	
	def mergeSortHelper(self, list1, list2):
		list1Len = len(list1)
		list2Len = len(list2)
		if list1Len <= 1 and list2Len <= 1:
			print(f"comparing {list1} and {list2}")
			return sorted(list1 + list2, key = lambda x: grocDict[x])
		
		if list1Len > 1:
			list1 = self.mergeSortHelper(list1[0:int(list1Len / 2)], list1[int(list1Len / 2):])
			
		if list2Len > 1:
			list2 = self.mergeSortHelper(list2[0:int(list2Len / 2)], list2[int(list2Len / 2):])
		
		list1Index = 0
		list2Index = 0	
		tempList = []
	
		print(f"The lists are {list1} and {list2}")
	
		for _ in range(list1Len + list2Len - 1):
			print(f"comparing {list1[list1Index]} and {list2[list2Index]}")
			if grocDict[list1[list1Index]] < grocDict[list2[list2Index]]:
				tempList.append(list1[list1Index])
				list1Index = list1Index + 1
				
				if list1Index == list1Len:
					tempList.extend(list2[list2Index:])
					break
			else:
				tempList.append(list2[list2Index])
				list2Index = list2Index + 1
			
				if list2Index == list2Len:
					tempList.extend(list1[list1Index:])
					break
				
				
		return tempList
	
	
	def mergeSort(self, listToSort):
		listLen = len(listToSort)
		return self.mergeSortHelper(listToSort[0:int(listLen / 2)], listToSort[int(listLen / 2):])	
	


class MainWindow(QMainWindow):
	def __init__(self, name = "My App", buttonText = "Click Me!", x = 500, y = 500):
		super().__init__()
		
		self.buttonIsChecked = True

		
		self.table = QTableWidget()

		self.layout = QGridLayout()
		
		self.setWindowTitle(name);
		self.button = QPushButton(buttonText)

		self.w2 = None

		self.button.clicked.connect(self.createNewWindow)

		self.container = QWidget()
		
		self.labelWidgets = []
		
		self.setFixedSize(QSize(x, y))
	
	def createNewWindow(self):
		if self.w2 == None:
			self.w2 = SecondWindow()
		self.w2.show()

	def theButtonWasClicked(self):
		item = self.input.text()
		#self.label.setText(text)
		displayAisleOfItem(self, entryList, item)
		#self.button.setText("You already clicked me moron.")

	def theWindowTitleChanged(self):
		print("title has changed")	

	def addButton(self, posy, posx, lenx, leny):
		self.layout.addWidget(self.button, posy, posx, lenx, leny)

	def addEntry(self, val, posy, posx, lenx = 1, leny = 1):
		label = QLabel()
		label.setText(str(val))
		self.labelWidgets.append(label)
		self.layout.addWidget(self.labelWidgets[(len(self.labelWidgets) - 1)], posy, posx, lenx, leny)
		return len(self.labelWidgets) - 1	#return the index of the widget

	def changeEntry(self):
		for n in range(len(self.labelWidgets)):
			pass	
			
	def setGUI(self):
		self.container.setLayout(self.layout)
		self.setCentralWidget(self.container)

	def swapEntry(self, index1, index2):
		text1, text2 = self.labelWidgets[index1].text(), self.labelWidgets[index2].text()
		self.labelWidgets[index1].setText(text2)
		self.labelWidgets[index2].setText(text1)
		


def swapLabels(index1, index2):
	window.swapEntry(index1, index2)
	print("swap")
	window.setGUI()

def addListToGUI(window, groceryList):
	row = 0
	window.table.setRowCount(len(groceryList))
	longestCol = 0
	for aisle in groceryList:
		if(len(aisle) > longestCol):
			longestCol = len(aisle)
	
	window.table.setColumnCount(longestCol)	

	for aisle in groceryList:
		column = 0
		for item in aisle:
			entry = QTableWidgetItem(item)
			window.table.setItem(row, column, entry)
			column += 1
		row += 1
	
	window.table.resizeColumnsToContents()
	#window.table.resizeRowToContents()

	window.layout.addWidget(window.table)
	window.setGUI()




app = QApplication([])


window = MainWindow("Grocery", "Click Me!")

window.addButton(0, 0, 1, 10)

addListToGUI(window, grocList)

window.setGUI()

window.show()

app.exec()

