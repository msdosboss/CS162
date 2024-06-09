import pytest
import random


def outputListToFile(sortedList):
	with open("groceryList", "w") as f:
		
		for n, aisle in enumerate(sortedList):
			f.write(f"aisle {n + 1}: ")
			for index, item in enumerate(aisle):
				f.write(item)
				if index != len(aisle) - 1:
					f.write(", ")
			f.write("\n")

def testOutputListToFile():
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
	itemList = []
	testList = []
	for aisleNumber in range(random.randrange(1, len(grocList))):
		for itemNumber in range(random.randrange(0, len(grocList[aisleNumber]))):
			itemList.append(grocList[aisleNumber][itemNumber])
		testList.append(itemList)
		itemList = []	
	
	outputListToFile(testList)
	
	with open("groceryList", "r") as f:
		for i, aisle in enumerate(testList):
			fileOutput = f.readline()
			print(fileOutput)
			if aisle == []:
				print(f"aisle {i + 1}:")
				print(fileOutput)
				assert fileOutput == f"aisle {i + 1}: \n"
			else:
				for item in aisle:
					assert item in aisle


