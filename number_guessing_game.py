import random
x = random.randint(0, 100)
attempts = 0

print("Guess a number between 0 and 100. ")
while attempts < 10:
    guess = input("What's your guess? ")

    attempts += 1

    if guess < x:
        print("The number is higher.")
    if guess > x:
        print("The number is lower.")
    if guess == x:
        print("You guessed the number in " + str(attempts) + " tries.")
        break

if guess != x:
    x = str(x)
    print("The number was actually " + x + " .")

