def output1(x,y):
    if x > y :
        print("x")
    elif y > x :
        print("y")    
    else:
        print("XY")

def output2():
    for i in range(5):
        print(i)

def output2_1():
    i = 0
    while i < 5:
        print (i)
        i += 1

def output3():
    for i in range(3):
        for q in range(3):   
            print((i,q))

def output4():
    while True:
        print(1)
        print(2)
        print(3)
        break

class A:
    def __init__(self, a):
        self.a = a

    def setA(self,a):
        self.a = a

    def getA(self):
        return self.a    

a = A("A")
a.setA("a")

b = A("B")
b.setA("b")