import random

# Soldier
class Soldier:
    def __init__(self,health,strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength
    
    def receiveDamage(self,damage):
        self.health = self.health - damage

# Viking
class Viking:
    def __init__(self,name,health,strength):
        Soldier.__init__(self,health,strength)
        self.name = name
    
    def attack(self):
        return self.strength
        # return super().attack()

    def receiveDamage(self, damage):
        self.health = self.health - damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"
    
    def battleCry(self):
        return "Odin Owns You All!"

# Saxon
class Saxon:
    def __init__(self,health,strength):
        Soldier.__init__(self, health, strength)
    
    def attack(self):
        return self.strength
    
    def receiveDamage (self,damage):
        self.health = self.health - damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return "A Saxon has died in combat"

# War
class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking (self,Viking):
        self.vikingArmy.append(Viking)
    
    def addSaxon (self,Saxon):
        self.saxonArmy.append (Saxon)
    
    def vikingAttack(self):
        viking1 = random.choice(self.vikingArmy)
        saxon1 = random.choice (self.saxonArmy)
        saxonDamage = saxon1.receiveDamage(viking1.attack()) #viking attack = viking strength
        if saxon1.health <= 0:
            self.saxonArmy.remove(saxon1)
            return saxonDamage
    
    def saxonAttack(self):
        viking2 = random.choice(self.vikingArmy)
        saxon2 = random.choice (self.saxonArmy)
        vikingDamage = viking2.receiveDamage(saxon2.attack()) 
        if viking2.health <= 0:
            self.saxonArmy.remove(viking2)
            return vikingDamage
    
    def showStatus (self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        else: 
            return "Vikings and Saxons are still in the thick of battle."