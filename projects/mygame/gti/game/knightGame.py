
from random import choice

class Knight:
    healthPoints = 30
    evasion = 7
    attackFuryWhip = 1
    attackDoubleSwing = choice ((2,4))
    attackPowerStrike = choice ((4, 7))

class Hydra:
    name = "Hydra"
    healthPoints = choice((2,5)) 
    attack = healthPoints


class Goblin:
    name = "Goblin"
    healthPoints = 6
    attack = 3
    
class Mercenary:
    name = "Mercenary"
    healthPoints = choice ((5,12))
    attackWhip = choice ((1,2))
    attack = choice ((3,5))
    

class Troll:
    name = "Troll"
    healthPoints = choice ((10, 15))
    attack = choice ((7, 10))
    
class Cat:
    name = "Cat"
    healthPoints = choice ((6, 10))
    attack = choice ((4, 7))
    
class Whisard:
    name = "Wisard"
    healthPoints = choice ((5, 9))
    attack = choice ((5, 9))
    

class Weirdo:
    name = "Weirdo"
    healthPoints = choice ((6, 12))
    attack = choice ((4, 10))


playing = True

#hero
knight = Knight()

#villains
hydra = Hydra()
goblin = Goblin()
mercenary = Mercenary()
troll = Troll()
cat = Cat()
whisard = Whisard()
weirdo = Weirdo()

villains = [hydra, goblin, mercenary, troll, cat, whisard, weirdo]
round = 1

def picVillain():
    vSize = len(villains) - 1
    return villains[choice((0,vSize))]    

#def battle(hero,villian):
    print("Hero > Villain")
    print("\t Hero attacks power =", hero.attackFuryWhip)
    print("\t Villian =", villian.name)
    print("\t Villian current HP =", villian.healthPoints) 
    dammage =  villian.healthPoints- hero.attackFuryWhip  
    villian.healthPoints = dammage
    print("\t Villian new HP =", villian.healthPoints)
    print("Villain > Hero")
    villainAttack = villain.attacks[0]
    print("\t Villain attacks power =", villainAttack)
    print("\t Hero current HP =", hero.healthPoints)
    dammageHero = hero.healthPoints - villainAttack
    hero.healthPoints = dammageHero
    print("\t Hero new HP =", hero.healthPoints)

while playing:

    print ("================ Round", round," ================= ")
    print ("#### Hero #### ")
    print ("HP =", knight.healthPoints)
    print ("Fury Whip =", knight.attackFuryWhip)
    print ("Double Swing =", knight.attackDoubleSwing)
    print ("Power Strike =",knight.attackPowerStrike)

    print("#### Hydra ####")
    print("HP =", hydra.healthPoints)

    print("#### Goblin #### ")
    print("HP =", goblin.healthPoints)

    print("#### Mercenary #### ")
    print("HP =", mercenary.healthPoints)

    print("#### Troll ####")
    print("HP =", troll.healthPoints)

    print("#### Cat ####")
    print("HP =", cat.healthPoints)

    print("#### Whisard ####")
    print("HP =", whisard.healthPoints)

    print("#### Weirdo ####")
    print("HP =", weirdo.healthPoints)

    # Display hero menu
    # Here the Knigth attacks the villan
    attack = input("Choose the Hero's attack: 0, 1, 2 \n")
    dammage = 0
    if attack == "0":
        qtdVillainPicked = choice((2,5))
        print("Qtd Villains= ",qtdVillainPicked)
        for x in range(qtdVillainPicked):
            villain = picVillain()
            # hero attacks villain
            damage = villain.healthPoints- knight.attackFuryWhip
            print("Villain =", villain.name)
            print("Hero attacks power =", knight.attackFuryWhip)
            villain.healthpoints = damage     
             
    elif attack == "1":
        qtdVillainPicked = choice((2))
        dammage =  villain.healthPoints- knight.attackDoubleSwing  
        print("Villian 1 =", villain.name)
        print("Hero attacks power =", knight.attackDoubleSwing)
        villain.healthPoints = dammage  

    elif attack == "2":
        villain = picVillain()
        damage = villain.healthpoints- knight.attackPowerStrike
        print("Villain =", villain.name)
        print("Hero attacks power =", knight.attackPowerStrike)
        villain.healthpoints = damage

    # Here the villan attacks the Knigth
    attackValue = 0
    for v in villains:
        if v.name == "Mercenary":
            mercenaryRandomAttack = choice((0,1))
            if mercenaryRandomAttack == 0 :
               knight.evasion -= choice((1,2))
            else:
                attackPercentage = (v.attack*knight.evasion) / 100
                dammagePercentage = (knight.healthPoints * attackPercentage) 
                knight.healthPoints = knight.healthPoints - dammagePercentage   
        else:
            attackPercentage = (v.attack*knight.evasion) / 100
            dammagePercentage = (knight.healthPoints * attackPercentage) 
            knight.healthPoints = knight.healthPoints - dammagePercentage 
    
    if hydra.healthPoints > 0 :
        hydra.healthPoints += 1
   
    if knight.healthPoints < 0:
        print(" +++++++++++++++++++++++++++++")
        print("     G A M E     O V E R")
        print(" +++++++++++++++++++++++++++++")
        break

    round = round +1
 
print("************ END ************")
print("#### Hero #### ")
print("HP =", knight.healthPoints)
print("#### Hydra #### ")
print("HP =", hydra.healthPoints)
print("#### Goblin #### ")
print("HP =", goblin.healthPoints)
print("### Mercenary ###")
print("HP =", mercenary.healthPoints)
print("### Troll ###")
print("HP =", troll.healthPoints)
print("### Cat ###")
print("HP =", cat.healthPoints)
print("### Whisard ###")
print("HP =", whisard.healthPoints)
print("### Weirdo ###")
print("HP =", weirdo.healthPoints)