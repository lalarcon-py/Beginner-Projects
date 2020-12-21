import random
import time


roll_again = "Yes"

dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)
while roll_again == "Yes" or "y":
    print("\nRolling the dice...")
    time.sleep(1)
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    print("The values are...")
    print("Dice 1 =", dice1, "\nDice 2 =", dice2)
    if dice1 == dice2:
        print("You rolled doubles!")
    else:
        print("Keep goin'!")
    roll_again = input("\nRoll the dice again? (Y/N)")



