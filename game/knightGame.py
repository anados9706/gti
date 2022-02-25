
from random import choice

class Knight:
    HP = 30
    evasion = 7
    attackFuryWhip = 1
    attackDoubleSwing = choice ((2,4))
    attackPowerStrike = choice ((4, 7))

class Hydra:
<<<<<<< HEAD
    HP = 1
    attack = 1    

class Goblin:
    name = "Goblin"
    HP = 6
    attackStab = 3
    attacks = [attackStab]

=======
    name = "Hydra"
    healthPoints = choice((2,5)) 
    attack = healthPoints


class Goblin:
    name = "Goblin"
    healthPoints = 6
    attack = 3
    
>>>>>>> 17c4c698013546ea8a346f7081a8a1ed85e5826b
class Mercenary:
    name = "Mercenary"
    HP = choice ((5,12))
    attackWhip = choice ((1,2))
    attack = choice ((3,5))
    

class Troll:
    name = "Troll"
<<<<<<< HEAD
    HP = choice ((10, 15))
    attackSwingClub = choice ((7, 10))
    attacks = [attackSwingClub]
=======
    healthPoints = choice ((10, 15))
    attack = choice ((7, 10))
>>>>>>> 17c4c698013546ea8a346f7081a8a1ed85e5826b
    
class Cat:
    name = "Cat"
<<<<<<< HEAD
    HP = choice ((6, 10))
    attackScratch = choice ((4, 6))

class Whisard:
    name = "Wisard"
    HP = choice ((5, 9))
    attackDarkPower = choice ((5, 7))

class Weirdo:
    name = "Weirdo"
    HP = choice ((6, 12))
    attackBananas = choice ((4, 6))
=======
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

>>>>>>> 615c1b97660de625508ba69510778ab4695e48e0

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

    print ("================= Round", round," ================= ")
    print ("#### Hero #### ")
    print ("HP =", knight.HP)
    print ("Fury Whip =", knight.attackFuryWhip)
    print ("Double Swing =", knight.attackDoubleSwing)
    print ("Power Strike =",knight.attackPowerStrike)

<<<<<<< HEAD
    print("#### Hydra #### ")
    print("HP =", hydra.HP)
=======
    print("#### Hydra ####")
    print("HP =", hydra.healthPoints)
>>>>>>> 17c4c698013546ea8a346f7081a8a1ed85e5826b

    print("#### Goblin #### ")
    print("HP =", goblin.HP)

    print("#### Mercenary #### ")
    print("HP =", mercenary.HP)

    print("#### Troll ####")
    print("HP =", troll.HP)

    print("#### Cat ####")
<<<<<<< HEAD
    print("HP =", cat.HP)
=======
    print("HP =", cat.healthPoints)
>>>>>>> 17c4c698013546ea8a346f7081a8a1ed85e5826b

    print("#### Whisard ####")
    print("HP =", whisard.HP)

    print("#### Weirdo ####")
    print("HP =", weirdo.HP)

    # Display hero menu
    # Here the Knigth attacks the villan
    attack = input("Choose the Hero's attack: 0, 1, 2 \n")
    dammage = 0
    if attack == "0":
<<<<<<< HEAD
        villian = picVillain()
        dammage =  villian.HP- knight.attackFuryWhip  
        print("Villian =", villian.name)
        print("Hero attacks power =", knight.attackFuryWhip)  
        villian.HP = dammage 
=======
        qtdVillainPicked = choice((2,5))
        print("Qtd Villains= ",qtdVillainPicked)
        for x in range(qtdVillainPicked):
            villain = picVillain()
<<<<<<< HEAD
            battle(knight,villain)
           
>>>>>>> 615c1b97660de625508ba69510778ab4695e48e0
             
    elif attack == "1":
        villian = picVillain()
        dammage =  villian.HP- knight.attackDoubleSwing  
        print("Villian 1 =", villian.name)
        print("Hero attacks power =", knight.attackDoubleSwing)
        villian.HP = dammage  

        villian = picVillain()
        dammage =  villian.HP- knight.attackDoubleSwing  
        print("Villian 2 =", villian.name)
        print("Hero attacks power =", knight.attackDoubleSwing)  
        villian.HP = dammage 
=======
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
>>>>>>> 17c4c698013546ea8a346f7081a8a1ed85e5826b

    elif attack == "2":
        villain = picVillain()
        damage = villain.HP- knight.attackPowerStrike
        print("Villain =", villain.name)
        print("Hero attacks power =", knight.attackPowerStrike)
<<<<<<< HEAD
        villain.HP = damage

    # Here the villan attacks the Knigth
    #dammage = knight.healthPoints - goblin.attackStab
    #dammage = knight.healthPoints - picVillain() 
<<<<<<< HEAD
    dammage = knight.HP - (hydra.attack + goblin.attackStab + mercenary.attackSwing + troll.attackSwingClub + cat.attackScratch + whisard.attackDarkPower + weirdo.attackBananas)
    print("villains attacks power=", goblin.attackStab + mercenary.attackSwing + troll.attackSwingClub + cat.attackScratch + whisard.attackDarkPower + weirdo.attackBananas)
    #print("villains attacks power=", 
    knight.HP = dammage
=======
    #dammage = knight.healthPoints - (goblin.attackStab + mercenary.attackSwing + troll.attackSwingClub + cat.attackScratch + turtle.attackTurtleShell + whisard.attackDarkPower + weirdo.attackBananas)
    #print("villains attacks power=", goblin.attackStab + mercenary.attackSwing + troll.attackSwingClub + cat.attackScratch + turtle.attackTurtleShell + whisard.attackDarkPower + weirdo.attackBananas)
    #print("villains attacks power=", 
    #knight.healthPoints = dammage
>>>>>>> 615c1b97660de625508ba69510778ab4695e48e0

=======
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
>>>>>>> 17c4c698013546ea8a346f7081a8a1ed85e5826b
    
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
<<<<<<< HEAD
print("HP =", knight.HP)
print("#### Hydra #### ")
print("HP =", hydra.HP)
=======
print("HP =", knight.healthPoints)
print("#### Hydra #### ")
print("HP =", hydra.healthPoints)
>>>>>>> 17c4c698013546ea8a346f7081a8a1ed85e5826b
print("#### Goblin #### ")
print("HP =", goblin.HP)
print("### Mercenary ###")
print("HP =", mercenary.HP)
print("### Troll ###")
print("HP =", troll.HP)
print("### Cat ###")
<<<<<<< HEAD
print("HP =", cat.HP)
=======
print("HP =", cat.healthPoints)
>>>>>>> 17c4c698013546ea8a346f7081a8a1ed85e5826b
print("### Whisard ###")
print("HP =", whisard.HP)
print("### Weirdo ###")
print("HP =", weirdo.HP)