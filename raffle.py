import random
participants = int(input("How many people do you want to enter in this raffle? "))
prize = input("What is the prize? ")
drawings = []

while len(drawings) < participants:
    people = input("Name one of the participants. ")
    drawings.append(people)

winner = random.choice(drawings)
print(str(winner) + " wins " + str(prize) + "!")
    

