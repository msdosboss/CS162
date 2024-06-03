from PyQt6.QtCore import QSize, Qt, QTimer
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QGridLayout
import pytest
import time
import random

defaultLabelText = "orca"

class MainWindow(QMainWindow):
	def __init__(self, name = "My App", buttonText = "Click Me!", x = 1000, y = 1000):
		super().__init__()
		
		self.buttonIsChecked = True

		self.input = QLineEdit()
		
		self.layout = QGridLayout()
		
		self.setWindowTitle(name);
		self.button = QPushButton(buttonText)



		self.container = QWidget()
		
		self.labelWidgets = []
		
		self.setFixedSize(QSize(x, y))
	
	def theButtonWasClicked(self):
		item = self.input.text()
		#self.label.setText(text)
		displayAisleOfItem(self, entryList, item)
		#self.button.setText("You already clicked me moron.")

	def theWindowTitleChanged(self):
		print("title has changed")	

	def addButton(self, posx, posy, lenx, leny):
		self.layout.addWidget(self.button, posx, posy, lenx, leny)

	def addEntry(self, val, posx, posy, lenx = 1, leny = 1):
		label = QLabel()
		label.setText(str(val))
		self.labelWidgets.append(label)
		self.layout.addWidget(self.labelWidgets[(len(self.labelWidgets) - 1)], posx, posy, lenx, leny)
		return len(self.labelWidgets)	#return the index of the widget

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
		

def mergeSortHelperGUI(list1, list2, widgetList1Index, widgetList2Index):
	list1Len = len(list1)
	list2Len = len(list2)
	if list1Len <= 1 and list2Len <= 1:
		if int(list1[0].text()) < int(list2[0].text()):
			return list1 + list2
		else:
			QTimer.singleShot(5000, lambda: swapLabels(widgetList1Index, widgetList2Index))
			window.show()
			return list2 + list1
	
	if list1Len > 1:
		list1 = mergeSortHelperGUI(list1[0:int(list1Len / 2)], list1[int(list1Len / 2):], widgetList1Index, (widgetList1Index + int(list1Len / 2)))
		
	if list2Len > 1:
		list2 = mergeSortHelperGUI(list2[0:int(list2Len / 2)], list2[int(list2Len / 2):], widgetList2Index, (widgetList2Index + int(list2Len / 2)))
	
	list1Index = 0
	list2Index = 0	
	tempList = []

	for _ in range(list1Len + list2Len - 1):
		if int(list1[list1Index].text()) < int(list2[list2Index].text()):
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


def mergeSortGUI(listToSort):
	listLen = len(listToSort)
	return mergeSortHelperGUI(listToSort[0:int(listLen / 2)], listToSort[int(listLen / 2):], 0, int(listLen / 2))	



def mergeSortHelper(list1, list2):
	list1Len = len(list1)
	list2Len = len(list2)
	if list1Len <= 1 and list2Len <= 1:
		print(f"comparing {list1} and {list2}")
		return sorted(list1 + list2)
	
	if list1Len > 1:
		list1 = mergeSortHelper(list1[0:int(list1Len / 2)], list1[int(list1Len / 2):])
		
	if list2Len > 1:
		list2 = mergeSortHelper(list2[0:int(list2Len / 2)], list2[int(list2Len / 2):])
	
	list1Index = 0
	list2Index = 0	
	tempList = []

	print(f"The lists are {list1} and {list2}")

	for _ in range(list1Len + list2Len - 1):
		print(f"comparing {list1[list1Index]} and {list2[list2Index]}")
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

def testMergeSort():
	testList = [4, 2, 1, 6]
	assert [1, 2, 4, 6] == mergeSort(testList)

def swapLabels(index1, index2):
	window.swapEntry(index1, index2)
	print("swap")
	window.setGUI()


app = QApplication([])

window = MainWindow("Number searcher", "iterate")

numList = [5, 1, 3, 1, 10, 4, 15, 12, 2, 5, 21, 100, 2]

print(mergeSort(numList))

window.addButton(0, 0, 1, 10)

for n in range(100):
	window.addEntry(random.randrange(0, 100), (n // 10) + 1, n % 10)

window.setGUI()

window.show()

QTimer.singleShot(1000, lambda: swapLabels(0, 10))

window.labelWidgets = mergeSortGUI(window.labelWidgets)



print("merge finished")

window.setGUI()

window.show()

app.exec()

