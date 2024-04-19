import random


class armor:
    def __init__(self, name, resist):
        self.name = name
        self.resist = resist

class player:
    def __init__(self, name, health = 10):
        self.name = name
        self.health = health
        self.items = {
            "potion" : 0,
            "1upmushroom" : 0,
            "pokeball" : 0,
            "thunderfuryblessedbladeofthewindseeker" : 0
        }
        self.head = armor("head", "0")
        self.chest = armor("chest", "0")
        self.pants = armor("pants", "0")
        self.boots = armor("boots", "0")
    
    def addItem(self, item):
        if item in self.items:
            self.items[item] += 1
            return 0
        else:
            print("item not in dict")
            return 1
    
    def listItems(self):
        keyList = list(self.items.keys())
        valueList = list(self.items.values())
        for x in range(len(keyList)):
            if valueList[x] == 0:
                continue
            elif valueList[x] == 1:
                print(f"\n{self.name} has {valueList[x]} {keyList[x]} \n")
            else:
                print(f"\n{self.name} has {valueList[x]} {keyList[x]}s\n")
    
    def addArmor(self, slot, name, resist):
        match slot:
            case "head":
                self.head.name = name
                self.head.resist = resist
                return 0
            case "chest":
                self.chest.name = name
                self.chest.resist = resist
                return 0
            case "pants":
                self.pants.name = name
                self.pants.resist = resist
                return 0
            case "boots":
                self.boots.name = name
                self.boots.resist = resist
                return 0
            case _:
                print("not valid slot")
                return 1
    
    def listArmor(self):
        if self.head.name != "head":                                             #I get that this is pretty non dynamic, but I figured designers would not just be adding a bunch of armor slots unlike they would with items. That is why I decided to take a more dynamic apporch with listItems()
            print("The helemt the player has equiped is " + self.head.name)
        if self.chest.name != "chest":
            print("The chest the player has equiped is " + self.chest.name)
        if self.pants.name != "pants":
            print("The pants the player has equiped are " + self.pants.name)
        if self.boots.name != "boots":
            print("The boots the player has equiped are " + self.boots.name)    




def addItemFromGods(godItems, armor, player):
    chosenItem = input(f"Enter 0 if you would like a {godItems['0']}\nEnter 1 if you would like a {godItems['1']}\nEnter 2 if you would like a {armor}: ")
    if chosenItem == "2":
        player.addArmor(godItems[chosenItem], armor, 1)
    elif chosenItem == "1" or chosenItem == "0":
        player.addItem(godItems[chosenItem])
    else:
        print("You have enterd an invalid input and have displeased the gods, they smite you and you lose 1 hp")
        player.health -= 1 

def testName(playerObject, expectedName):
    return (playerObject.name == expectedName)

def testHealth(playerObject, expectedHealth):
    return (playerObject.health == expectedHealth)

def testItems(playerObject, itemsList):
    count = 1
    for x in range(len(itemsList)):
        if x != len(itemsList) - 1:
            if itemsList[x] != itemsList[x + 1]:
                if count != playerObject.items[itemsList[x]]:
                    return False
                count = 0
            count += 1
        else:
            if count != playerObject.items[itemsList[x]]:
                return False

    return True

def testPlayer(name, health, itemsList):
    '''Creates a player object, populates the attributes then tests those atributes to make sure they have the correct values'''
    testPlayer = player(name, health)
    if testName(testPlayer, name) == False:
        return 1
    
    if testHealth(testPlayer, health) == False:
        return 2

    for x in range(len(itemsList)):
        if testPlayer.addItem(itemsList[x]) == 1:
            return 3


    testPlayer.listItems()
    itemsList.sort()        #the item test relies on each of the duplicate items to be next to each other in the list
    
    if testItems(testPlayer, itemsList) == False:
        return 4
    
    return 0



print(testPlayer("orca", 15,["potion", "1upmushroom", "potion"]))
    

'''player1 = player(input("What is your name?: "))

print("Nice to meet you", player1.name, "I wish you luck")

flag = 0

while flag == 0 or health <= 0:
    print(player1.name, "has enterd the room that holds the council of gods.\n")
    print("The Gods are quite pleased with your work and offer you a choice in items.\n")
    if random.randrange(100) % 2 == 0:
        godItems = {                        #This probably could have been an array
            "0" : "potion",
            "1" : "thunderfuryblessedbladeofthewindseeker",
            "2" : "head"
        }
        addItemFromGods(godItems, "Bike Helmet", player1)

    else:
        godItems = {                        #This probably could have been an array
            "0" : "1upmushroom",
            "1" : "pokeball",
            "2" : "boots"
        }
        addItemFromGods(godItems, "Gucci Flip Flops", player1)
    
    player1.listItems()
    player1.listArmor()

    quitflag = input("\nWould you like to quit y/n: ")
    if quitflag == "y":
        print("Goodbye")
        break
'''
