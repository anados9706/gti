
class Golem:
    def __init__(self, name, type, catchphase = None) -> None:
       self.name = name
       self.type = type
       self.catchphase = catchphase
    def sayHello(self):
        print("Hey, my name is " + self.name + " I'm a Goblim.")
    def sayCatchPhase(self):
        print("I'm the coolest Golem in the world!!")
    def getType(self):
        return self.type

if __name__ == "__main__":       
    doug = Golem("Doug", "made out of clay")     
    doug.sayHello()
    print("What type of Golem is Doug?" + doug.getType())
doug.sayCatchPhase()

print()