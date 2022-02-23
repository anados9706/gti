
from random import choice

class Knight:
    healthPoints = 30
    evasion = 7
    attackFuryWhip = 1
    attackDoubleSwing = choice ((2,4))
    attackPowerStrike = choice ((4, 7))

class Goblin:
    name = "Goblin"
    healthPoints = 6
    attackStab = 3

class Mercenary:
    name = "Mercenary"
    healthPoints = choice ((5,12))
    attackWhip = choice ((1,2))
    attackSwing = choice ((3,5))

class Troll:
    name = "Troll"
    healthPoints = choice ((10, 15))
    attackSwingClub = choice ((7, 10))
    
class Cat:
    name = "Cat"
    healthPoints = choice ((6, 10))
    attackScratch = choice ((4, 7))

class Turtle:
    name = "Turtle"
    healthPoints = choice ((5, 10))
    attackTurtleShell = choice ((5, 7))

class Whisard:
    name = "Wisard"
    healthPoints = choice ((5, 9))
    attackDarkPower = choice ((5, 9))

class Weirdo:
    name = "Weirdo"
    healthPoints = choice ((6, 12))
    attackBananas = choice ((4, 10))

playing = True

#hero
knight = Knight()

#villains
goblin = Goblin()
mercenary = Mercenary()
troll = Troll()
cat = Cat()
turtle = Turtle()
whisard = Whisard()
weirdo = Weirdo()

villains = [goblin, mercenary, troll, cat, turtle, whisard, weirdo]
round = 1

def picVillain():
    vSize = len(villains) - 1
    return villains[choice((0,vSize))]    

while playing:

    print ("================= Round", round," ================= ")
    print ("#### Hero #### ")
    print ("HP =", knight.healthPoints)
    print ("Fury Whip =", knight.attackFuryWhip)
    print ("Double Swing =", knight.attackDoubleSwing)
    print ("Power Strike =",knight.attackPowerStrike)

    print("#### Goblin #### ")
    print("HP =", goblin.healthPoints)

    print("#### Mercenary #### ")
    print("HP =", mercenary.healthPoints)

    print("#### Troll ####")
    print("HP =", troll.healthPoints)

    print("#### Cat ####")
    print("HP =", cat.healthPoints)

    print("#### Turtle ####")
    print("HP =", turtle.healthPoints)

    print("#### Whisard ####")
    print("HP =", whisard.healthPoints)

    print("#### Weirdo ####")
    print("HP =", weirdo.healthPoints)

    # Display hero menu
    # Here the Knigth attacks the villan
    attack = input("Choose the Hero's attack: 0, 1, 2 \n")
    dammage = 0
    if attack == "0":
        villian = picVillain()
        dammage =  villian.healthPoints- knight.attackFuryWhip  
        print("Villian =", villian.name)
        print("Hero attacks power =", knight.attackFuryWhip)  
        villian.healthPoints = dammage 
             
    elif attack == "1":
        villian = picVillain()
        dammage =  villian.healthPoints- knight.attackDoubleSwing  
        print("Villian 1 =", villian.name)
        print("Hero attacks power =", knight.attackDoubleSwing)
        villian.healthPoints = dammage  

        villian = picVillain()
        dammage =  villian.healthPoints- knight.attackDoubleSwing  
        print("Villian 2 =", villian.name)
        print("Hero attacks power =", knight.attackDoubleSwing)  
        villian.healthPoints = dammage 

    elif attack == "2":
        villain = picVillain()
        damage = villain.healthpoints- knight.attackPowerStrike
        print("Villain =", villain.name)
        print("Hero attacks power =", knight.attackPowerStrike)
        villain.healthpoints = damage
       
       #Gato, oq eu fasso? uma lista so com poderes dos viloes e 
       # dai criar um DEF. com cada poder de cala vilao, pra dai aqui no final, 
       # quando forem atacar o eroi, o computador escolhe UM dos viloes e usa o 
       # poder desse vilao pra atacar o heroi, tipo u  PICK A VILLAIN, sabe.

    # Here the villan attacks the Knigth
    #dammage = knight.healthPoints - goblin.attackStab
    dammage = knight.healthPoints - picVillain() 
    #dammage = knight.healthPoints - (goblin.attackStab + mercenary.attackSwing + troll.attackSwingClub + cat.attackScratch + turtle.attackTurtleShell + whisard.attackDarkPower + weirdo.attackBananas)
    #print("villains attacks power=", goblin.attackStab + mercenary.attackSwing + troll.attackSwingClub + cat.attackScratch + turtle.attackTurtleShell + whisard.attackDarkPower + weirdo.attackBananas)
    #print("villains attacks power=", 
    knight.healthPoints = dammage

    
    round = round +1
 
print("************END************")
print("#### Hero #### ")
print("HP =", knight.healthPoints)
print("#### Goblin #### ")
print("HP =", goblin.healthPoints)
print("### Mercenary ###")
print("HP =", mercenary.healthPoints)
print("### Troll ###")
print("HP =", troll.healthPoints)
print("### Cat ###")
print("HP =", cat.healthPoints)
print("### Turtle ###")
print("HP =", turtle.healthPoints)
print("### Whisard ###")
print("HP =", whisard.healthPoints)
print("### Weirdo ###")
print("HP =", weirdo.healthPoints)