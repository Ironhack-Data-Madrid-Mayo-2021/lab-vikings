
# Soldier


class Soldier:
    def __init__ (self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage):
        self.health -= damage

# Viking


class Viking(Soldier):
    def __init__ (self, name, health, strength):
        self.name = name
        super().__init__ (health, strength)

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"

    def battleCry(self):
        return "Odin Owns You All!"

# Saxon


class Saxon(Soldier):
    def __init__ (self, health, strength):
        super().__init__ (health, strength)

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return f"A Saxon has died in combat"
    

# War

import random

class War:
    def __init__ (self):
        self.vikingArmy = []
        self.saxonArmy = []
    
    def addViking(self, vik):
        self.vikingArmy.append(vik)

    def addSaxon(self, sax):
        self.saxonArmy.append(sax)

    def vikingAttack(self):
        saxon_fighter = random.choice(self.saxonArmy)
        viking_fighter = random.choice(self.vikingArmy)

        saxon_newhealth = saxon_fighter.receiveDamage(viking_fighter.strength)

        if saxon_fighter.health <= 0:
            self.saxonArmy.remove(saxon_fighter)
        
        return saxon_newhealth

    def saxonAttack(self):
        saxon_fighter = random.choice(self.saxonArmy)
        viking_fighter = random.choice(self.vikingArmy)

        viking_newhealth = viking_fighter.receiveDamage(saxon_fighter.strength)

        if viking_fighter.health <= 0:
            self.vikingArmy.remove(viking_fighter)
        
        return viking_newhealth
    
    def showStatus(self):
        if len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        elif len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) >= 1 and len(self.saxonArmy) >=1:
            return "Vikings and Saxons are still in the thick of battle."

