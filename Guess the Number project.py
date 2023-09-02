print(' === Guess the Number ===')

num_of_tries = 0

while True:
  variable = 2000
  guessed_num = float(input('guess a number between 1 and 1 million > '))

  if guessed_num < variable:
    print('too low go up')
    num_of_tries+=1
    
  elif guessed_num > variable:
    print('too high go down')
    num_of_tries +=1
  
  elif guessed_num == variable:
    print('congratulations you have won after', num_of_tries, 'tries!')
    exit()

  else:
    break

print('That is beyond the scope')
