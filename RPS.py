import random
import re
while(1 < 2):
    print("\n")
    print("Rock, Paper, Scissors - Shoot!")
    userChoice = input("Choose your weapon. Rock, Paper, or Scissors: ")
    if not re.match("[Scissors, Paper, Rock]", userChoice):
        print('Rock, Scissors orPaper.')
        continue
     #Echo the user's choice
    print("You chose: "+ userChoice)
    choices = ['Rock', 'Paper', 'Scissors']
    opponentChoice = random.choice(choices)
    print("I chose: " + opponentChoice)
    if opponentChoice == str(userChoice):
        print("Tie! ")
    elif opponentChoice.upper =='Rock' and userChoice.upper == 'Scissors':
        print("Rock beats scissors, I win! ")
    elif opponentChoice.upper == 'Scissors' and userChoice.upper == 'paper':
        print("Scissors beats paper, you lose! ")
    elif opponentChoice.upper == 'Paper' and userChoice.upper == 'rock':
        print("Paper beats rock, I win! ")
    else:
        print("You win! ")
