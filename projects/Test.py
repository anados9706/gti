from random import randint

class World:
    def __init__(self):
        self.hero = Frog()
        self.villains = [Frog(), Frog(), Frog()]
    def heroTurn(self):
        self. hero.hydroBlast(self.villains)
        pass    
    def rest(self):
        pass
    def isEndGame(self):
        pass

def doesHit(ev):
    return randint(1, 100) > (ev * 2)

class Frog:
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

if __name__ == "__main__":
    world = World()
    world.start()
    if "n" == input:
        world = World()
        world.start()
    pass            