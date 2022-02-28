


class Wizard:
    def __init__(self, name, power, hat = None)  -> None:
       self.name = name
       self.power = power
       self.hat = hat
    def sayIntro(self):
        print("Hello, my name is " + self.name + " . I'm a wizard.")
    def hasHat(self):
        if self.hat is not None:
            return True
        else:
            return False 
    def cast(self):
        print(self.name + " casts " + self.power)    

if __name__ == "__main__":
    bob = Wizard("Bob", "5 pounds of Ice") 
    bob.sayIntro()
    print("Does Bob has a hat? " + str(bob.hasHat))
bob.cast()  

print()