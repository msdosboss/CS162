import tkinter as tk

class entry:
    def __init__(self, name, row):
        self.name = name
        self.row = row

def printAvailableItems(entryList):
    for x in range(len(entryList)):
        print(f"{entryList[x].name} is located in row {entryList[x].row}")

def printAvailableItemsGui(root, entryList):
    for x in entryList:
        label = tk.Label(root, text = f"{x.name} is in row {str(x.row)}")
        label.pack()


entryList = []

entryList.append(entry("Milk", 4))
entryList.append(entry("Yogurt", 4))
entryList.append(entry("Chicken Nuggets", 5))
entryList.append(entry("Apple", 6))
entryList.append(entry("Banana", 6))
entryList.append(entry("Chicken", 7))

#printAvailableItems(entryList)

root = tk.Tk()
root.geometry('300x200')
root.resizable(False, False)
root.title('availableItems')

printAvailableItemsGui(root, entryList)

root.mainloop()
