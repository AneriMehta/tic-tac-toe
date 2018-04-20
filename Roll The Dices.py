import random

min = 1
max = 6

roll_again= "y"

while roll_again == "y":
    print("Rolling The Dices...")
    print("The Values are...")

    print("Dice 1 :",random.randint(min,max))
    print("Dice 2 :",random.randint(min,max))

    roll_again = input("\nRoll the Dices Again ?\ny/n\n")
    print("----------------------------------")