import random

computeroptions = ['rock', 'paper', 'scissors']
usercounter = 0
computercounter = 0

while usercounter < 3 and computercounter < 3:
    userchoice = input('Choose between rock, paper, or scissors: ').lower()
    computerchoice = random.choice(computeroptions)
    
    print(f"Computer chose: {computerchoice}")
    
    if userchoice == computerchoice:
        print('It is a draw')

    elif userchoice == 'rock' and computerchoice == 'scissors':
        print('Rock beats scissors, you win')
        usercounter += 1

    elif userchoice == 'scissors' and computerchoice == 'rock':
        print('Rock beats scissors, you lose')
        computercounter += 1

    elif userchoice == 'rock' and computerchoice == 'paper':
        print('Paper wraps rock, you lose')
        computercounter += 1

    elif userchoice == 'paper' and computerchoice == 'rock':
        print('Paper wraps rock, you win')
        usercounter += 1

    elif userchoice == 'scissors' and computerchoice == 'paper':
        print('Scissors cut paper, you win')
        usercounter += 1

    elif userchoice == 'paper' and computerchoice == 'scissors':
        print('Scissors cut paper, you lose')
        computercounter += 1

    else:
        print('You typed an invalid input, please try again.')
        continue  # Skip incrementing the round in case of invalid input

    
    print(f"Score: You {usercounter} - Computer {computercounter}\n")

if usercounter == 3:
    print('Congrats, you won the game!')
elif computercounter == 3:
    print('Computer won the game. You lose.')
