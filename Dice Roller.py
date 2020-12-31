import random
import time

roll_again = True

dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)
while roll_again == True:
    roll_again = True
    print("Rolling the dice...")
    time.sleep(1)
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    print("The values are...")
    print("Dice 1 =", dice1, "\nDice 2 =", dice2)
    if dice1 == dice2:
        print("You rolled doubles!")
    else:
        print("Keep goin'!")
    roll_again1 = input("\nRoll the dice again? (Y/N)")
    if roll_again1 == "Y":
        continue
    elif roll_again1 != "Y":
        roll_again = False
    else:
        print("The answer wasn't Y/N. Try again.")
