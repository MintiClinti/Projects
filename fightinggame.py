class Player:
    def __init__(player, name):
        player.name = name


class Puncher(Player):
    def __init__(punch, name, health, energy, tech):
        super().__init__(name)
        punch.health = health
        punch.energy = energy
        punch.tech = tech
    
class Kicker(Player):
    def __init__(kick, name, health, energy, tech):
        super().__init__(name)
        kick.health = health
        kick.energy = energy
        kick.tech = tech


name1 = input("What is your name? ")
name2 = input("What is your name? ")

p1 = Player(name1)
p2 = Player(name2)
    
turn = 0

puncher = Puncher(p1.name, 120, 40, "Iron Hands")
kicker = Kicker(p2.name, 85, 40, "Lightning Fast")

while kicker.health > 0 or puncher.health > 0:
    if puncher.health == 0:
        print(str(kicker.name) + " is the winner!")
        break
    elif kicker.health == 0:
        print(str(puncher.name) + " is the winner!")
        break
    else:
        if turn % 2 == 0:
            move = input(str(puncher.name) +" , what is your move? 0 for attack, 1 for tech. ")
            if move == "0":
                kicker.health -= (10)
                print(str(puncher.name) + " lands a hook on " + str(kicker.name) + "!")
                print(str(kicker.name) + " has " + str(kicker.health) + " health!")
            elif move == "1" and puncher.energy > 0:
                kicker.health -= 15
                puncher.energy -= 8
                print(str(puncher.name) + " hardens his fists and bashes " + str(kicker.name) + "!")
                print(str(puncher.name) + " has " + str(puncher.energy) + " energy!")
                print(str(kicker.name) + " has " + str(kicker.health) + " health!")
            else:
                print("That is not a valid move.")
        if turn % 2 == 1:
            move = input(kicker.name +" , what is your move? 0 for attack, 1 for tech. ")
            if move == "0":
                puncher.health -= (15)
                print(str(kicker.name) + " lands a kick on " + str(puncher.name) + "!")
                print(str(puncher.name) + " has " + str(puncher.health) + " health!")
            elif move == "1" and kicker.energy > 0:
                kicker.energy -= 10
                puncher.health -= 30
                print(str(kicker.name) + " musters his stregth and strikes " + str(puncher.name) + "!")
                print(str(kicker.name) + " has " + str(kicker.energy) + " energy!")
                print(str(puncher.name) + " has " + str(puncher.health) + " health!")
            else:
                print("That is not a valid move.")
        
        turn += 1

        

        
    
   

    




    
