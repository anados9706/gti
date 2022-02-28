

from random import choice


class Knight:
    healthPoints = 30
    evasion = 7
    attackFuryWhip = 1
    attackDoubleSwing = choice((2,4))

class Goblin:
    name= "Goblin"
    healthPoints = 6
    attackStab = 3

class Mercenary:
    name= "Mercenary"
    healthPoints = choice((5,12))
    attackWhip = choice((1,2))
    attackSwing = choice((3,5))

playing = True

#hero
knight = Knight()

#villains
goblin = Goblin()
mercenary = Mercenary()

villains = [goblin,mercenary]
round = 1

def picVillain():
    vSize = len(villains) - 1
    return villains[choice((0,vSize))]

while playing:

    print("================= Round ",round," ================= ")
    print("#### Hero #### ")
    print("HP=", knight.healthPoints)
    print("Fury Whip=", knight.attackFuryWhip)
    print("Double Swing=", knight.attackDoubleSwing)

    print("#### Goblin #### ")
    print("HP=", goblin.healthPoints)

    print("#### Mercenary #### ")
    print("HP=", mercenary.healthPoints)

    # Display hero menu
    # Here the Knigth attacks the villan
    attack = input("Choose the Hero's attack: 0,1 \n")
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
       

    # Here the villan attacks the Knigth
    dammage = knight.healthPoints - goblin.attackStab
    print("gooblin attacks power=", goblin.attackStab)
    knight.healthPoints = dammage

    
    round = round +1
 
print("************END************")
print("#### Hero #### ")
print("HP=", knight.healthPoints)
print("#### Goblin #### ")
print("HP=", goblin.healthPoints)