import math

def Y2X(y):
    return y ** 2

def printY2X(y):
    print("*" * Y2X(y))

class Student():
    def __init__(self, name, gpa, loc):
        self.name = name
        self.gpa = gpa
        self. loc = loc
    def sayHello(self):
        print("Hello! My name is " + self.name + ".")    
    def setGPA(self, gpa):
        self.gpa = gpa
    def getGPA(self):
        return self.gpa
    def getLoc(self):
        return self.loc
    def setLoc(self, loc):
        self.loc = loc  
    def __repr__(self):
        return self.name + " (" +str(self.gpa) +")"        


if __name__ == "__main__":
    # Main "Method"
   a = 11
   for y in range(a):
       printY2X(y)

   for y in range(2,8):
       printY2X(y)
   
   students = []
   students.append(Student("Liz", 3.4, (1,1,1)))
   students.append(Student("Bob", 3.4, (1,1,1)))
   students.append(Student("Jasun", 3.4, (1,1,1)))
   students.append(Student("Vy", 3.4, (1,1,1)))
   students.append(Student("Sally", 3.4, (1,1,1)))

   for student in students:
       student.sayHello()

   print(students)