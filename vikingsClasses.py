
# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
        
    
    def attack(self):
        return self.strength
    

    def receiveDamage(self, damage):
        self.damage = damage
        self.health -=  self.damage


# Viking


class  Viking(Soldier):
    def __init__(self, name, health, strength):
        self.name = name
        super().__init__(health, strength)


    def attack(self):
        return self.strength

    def Viking(self, damage):
        self.damage = damage
        self.health -=  self.damage
        if self.health <= 0:
            return print("f {self.name} has died in act of combat")
        if self.health > 0:
            return print("f {self.name} has received {self.damage} points of damage")

    def battleCry(self):
        return print ("Odin Owns You All!")


# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)
    
    def attack(self):
        return self.strength
        
    def Saxon(self, damage):
        self.damage = damage
        self.health -=  self.damage
        if self.health <= 0:
            return print("A Saxon has died in combat")
        if self.health > 0:
            return print("f A Saxon has received {self.damage} points of damage")


    

# War


class War:
    vikingArmy = []
    saxonArmy = []

    def addViking(self, Viking):
        self.Viking = Viking
        vikingArmy.add(self.viking)
    
    def addSaxon(self, Saxon):
        self.Saxon = Saxon
        saxonArmy.add(self.Saxon)

    def vikingAttack(self):
        random.choice(saxonArmy).damage == random.choice(vikingArmy).strength
        if random.choice(saxonArmy).damage <= 0:
            saxonArmy.remove("random.choice(saxonArmy)")
        elif random.choice(saxonArmy).damage > 0:
            print(f"{random.choice(saxonArmy).damage)} of a {random.choice(saxonArmy)} with the {random.choice(vikingArmy).strength} of a {random.choice(vikingArmy})
           
    
    def saxonAttack(self):
        random.choice(vikingArmy).damage = random.choice(saxonArmy).strength
         if random.choice(vikingArmy).damage <= 0:
            saxonArmy.remove("random.choice(vikingArmy)")
        elif random.choice(vikingArmy).damage > 0:
            print(f"{random.choice(vikingArmy).damage)} of a {random.choice(vikingArmy)} with the {random.choice(saxonArmy).strength} of a {random.choice(saxonArmy})

    
    def showStatus(self):
        if len(saxonArmy) == 0:
            return print("Vikings have won the war of the century!")
        elif len(vikingArmy) == 0:
             return print("Saxons have fought for their lives and survive another day...")
        else:
            return print("Vikings and Saxons are still in the thick of battle.")

    


