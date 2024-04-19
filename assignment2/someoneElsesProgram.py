import math
class shape:
    def __init__(self,n,sideL):
        self.n = n
        self.sideL = sideL
        self.area = (self.n*self.sideL/(2*(math.tan(math.pi/self.n))/self.sideL))/2
x = True

def writeShape(shape, filename):
    try:
        f = open(filename, "w")
        f.write(f"{shape.n},{shape.sideL}")
    except:
        print("error")
        return 1

def readShape(filename):
    try:
        f = open(filename, "r")
        shapeTemplate = f.read()
        shapeTemplate = shapeTemplate.split(",")
        print(shapeTemplate)
        return shape(int(shapeTemplate[0]), float(shapeTemplate[1]))
    except:
        print("file is not real")
        return 1

while x:
    try:
        n = int(input('input an interger value for the number of sides of your regular polygon '))
        sideL = float(input('input the side length of your shape '))
        shape1 = shape(n,sideL)
        print('your shape\'s area is ',shape1.area)
        writeShape(shape1, "shape1.txt")
        shape2 = readShape("shape.txt")
        print("shape2 area is ", shape2.area)
        if bool(input('would you like to continue? (True/False) ')):
            break
    except:
        print('there was an error')
