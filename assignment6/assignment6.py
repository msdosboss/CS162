from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QGridLayout
import pytest
import time

defaultLabelText = "orca"

class MainWindow(QMainWindow):
	def __init__(self, name = "My App", buttonText = "Click Me!", x = 1000, y = 1000):
		super().__init__()
		
		self.buttonIsChecked = True

		#self.label = QLabel()
		#self.label.setText(defaultLabelText)
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
		#layout.addWidget(self.label)

		
		self.setFixedSize(QSize(x, y))
	
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

def addNumberListWidgets(window, n):
	labelWidgets = []
	layout = QGridLayout()
	textField = QLineEdit()
	button = QPushButton("Search")
	labelWidgets.append(textField)
	labelWidgets.append(button)
	layout.addWidget(textField, 0, 0, 1, 7)
	layout.addWidget(button, 0, 7, 1, 3)
	
	for x in range(n):
		label = QLabel()
		label.setText(str(x))
		labelWidgets.append(label)
		layout.addWidget(label, (x // 10) + 1, x % 10)
	container = QWidget()
	container.setLayout(layout)
	window.setCentralWidget(container)
	return labelWidgets
	
def highlightSelectedNumber(labelWidgets):
	inputText = labelWidgets[0].text()
	for labelWidget in labelWidgets[2:]:
		labelWidget.setStyleSheet("")
	
	for labelWidget in labelWidgets[2:]:
		labelWidget.setStyleSheet("background-color: cyan")
		app.processEvents()		#this is considerd bad practice I should have worked my function into the processEvent loop, but instead I am just forcing it to process all events right now https://www.pythonguis.com/faq/real-time-change-of-widgets
		time.sleep(1)
		if labelWidget.text() == inputText:
			break
		labelWidget.setStyleSheet("")

def testHighlightSelectedNumber():				#test the all possible inputs
	for testText in range(100):
		for labelWidget in labelWidgets[2:]:
			labelWidget.setStyleSheet("background-color: cyan")
			if labelWidget.text() == str(testText):
				break
			labelWidget.setStyleSheet("")
		assert labelWidgets[testText + 2].styleSheet() == "background-color: cyan"



def mergeSortHelper(list1, list2):
	list1Len = len(list1)
	list2Len = len(list2)
	if list1Len <= 1 and list2Len <= 1:
		return sorted(list1 + list2)
	
	if list1Len > 1:
		list1 = mergeSortHelper(list1[0:int(list1Len / 2)], list1[int(list1Len / 2):])
		
	if list2Len > 1:
		list2 = mergeSortHelper(list2[0:int(list2Len / 2)], list2[int(list2Len / 2):])
	
	list1Index = 0
	list2Index = 0	
	tempList = []

	for _ in range(list1Len + list2Len - 1):
		if list1[list1Index] < list2[list2Index]:
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


def mergeSort(listToSort):
	listLen = len(listToSort)
	return mergeSortHelper(listToSort[0:int(listLen / 2)], listToSort[int(listLen / 2):])	


#testDictionaryEntryList(entryList)

#printAvailableItems(entryList)

#app = QApplication([])

#window = QWidget()
#window = QPushButton("Click Me")
#window = MainWindow("Number searcher", "iterate")

numList = [5, 1, 3, 1, 10, 4, 15, 12, 2, 5, 21, 100, 2]

print(mergeSort(numList))

#window.button.clicked.connect(lambda: printNumList(window, numList))

#labelWidgets = addNumberListWidgets(window, 100)

#labelWidgets[1].clicked.connect(lambda: highlightSelectedNumber(labelWidgets))

#window.show()

#app.exec()

