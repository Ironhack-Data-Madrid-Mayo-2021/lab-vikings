import random
from vikingsClasses import Soldier, Viking, Saxon, War

classmates = ["Santi", "Borja", "Alvaro", "Victoria", "Olaya", "Cris"]

# Create a War object and we initialize both armies
def create_war(vikings_names, number_saxons):
    
    war = War()
    
    for name in vikings_names:
        war.vikingArmy.append(Viking(name, 100, 30))

    for saxon in range(number_saxons):
        war.saxonArmy.append(Saxon(50, 50))
    
    return war

# Game with a determine count of round
def game (war, rounds):
    print("WAR HAS BEGUN:")
    for r in range(rounds):
        print(war.vikingAttack())
        if war.saxonArmy == []:
            print(war.showStatus())
            break
        print(war.saxonAttack())
        if war.vikingArmy == []:
            print(war.showStatus())
            break          
        print(war.showStatus())
    
# Game till some team die!    
def deathmatch_game(war):
    print("WAR HAS BEGUN:")
    print("DEATHMATCH!")
    while True:
        print(war.vikingAttack())
        if war.saxonArmy == []:
            print(war.showStatus())
            break
        print(war.saxonAttack())
        if war.vikingArmy == []:
            print(war.showStatus())
            break              
        print(war.showStatus())

test_war = create_war(classmates, 7)


# status = game(test_war, 10)

status = deathmatch_game(test_war)