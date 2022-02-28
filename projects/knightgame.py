from random import randint

from Test import doesHit

class Knight:
    def __init__(self):
        self.hp = randint(2, 5)
        self.ev = randint(20, 49)
    def takeDamege(self, damage):
        if(doesHit(self.ev)):
            print("hits for " + damage + ".")
            self.hp = max(self.hp - damage, 0)
        else: 
            print("misses target")   

    def poison(self, enemy):
        if randint(0,1) > 0:
            enemy.takeDamege(5)   

    def hydroBlast(self, enemies):
        #two targets
        for i in range(2):
            idx = randint(0, len(enemies))   
            enemies[idx].takedamage(2) 

class Hydra:
    def __init__(self):
        self.hp = randint(2, 5)

class Goblin: 
    def __init__(self):
        self.hp = randint(6, 7)
                
class Mercenary:
    def __init__(self):
        self.hp = randint(5, 12)
        self.ev = randint(1, 2)

class Troll:

class LostCat:

class Wizard:

class Turtle: