import random
import time
import sys


while True:
  print('welcome')
  print('I am thinking of a number between 1-100')
  print()
  print()
  difficulty = input("choose a difficulty, 'easy' or 'hard': \n\n")

  randomnum = random.randint(1,100)

  if difficulty == 'easy':
    numoftries = 10

    while numoftries != 0:
      guess = int(input('enter a guess: '))

      if randomnum == 0:
        print('you have 0 lives, you lose!')
        break
      elif guess > randomnum:
        print('too high! ')
        numoftries-=1
        print(f'you have {numoftries} left')
      elif guess < randomnum:
        print('too low')
        numoftries-=1
        print(f'you have {numoftries} left')
      else:
        print('congrats')
        break
      
    restart = input('would you like to restart? (y/n): ')
    if restart == 'n':
      print('thanks for playing')
      break

  elif difficulty == 'hard':
    numoftries = 5
    
    while numoftries != 0:
      guess = int(input('enter a guess: '))

      if numoftries == 0:
        print('you have 0 lives, you lose!')
      elif guess > randomnum:
        print('too high! ')
        numoftries-=1
        print(f'you have {numoftries} left')
      elif guess < randomnum:
        print('too low')
        numoftries-=1
        print(f'you have {numoftries} left')
      else:
        print('congrats')
        break
      
    restart = input('would you like to restart? (y/n): ')
    if restart == 'n':
      print('thanks for playing')
      break

  else:
    print('you have selected an invalid option')
