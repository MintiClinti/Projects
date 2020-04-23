score = 0

question_1 = input("What do you call a group of crows? ")
answer_1 = "Murder"

if question_1.capitalize() == answer_1:
    print("Correct!")
    score += 25
else:
    print("Wrong!")

question_2 = input("What do you call a group of owls? ")
answer_2 = "Parliament"

if question_2.capitalize() == answer_2:
    print("Correct!")
    score += 25
else:
    print("Wrong!")

question_3 = input("What do you call a group of lions? ")
answer_3 = "Pride"

if question_3.capitalize() == answer_3:
    print("Correct!")
    score += 25
else:
    print("Wrong!")

question_4 = input("What do you call a group of bunnies? ")
answer_4 = "Fluffle"

if question_4.capitalize() == answer_4:
    print("Correct!")
    score += 25
else:
    print("Wrong!")

print("Your score was " + str(score) + " percent!")



