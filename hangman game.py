import random

list_of_words = ['day', 'time', 'junction', 'space', 'clean', 'stop']
letters_chosen = []
counter = 6
chosen_word = random.choice(list_of_words)

Title = '🌟HANGMAN🌟'
print(f'{Title:>30}')

while True:
    user_choice = input('choose a letter > ')
    if user_choice in letters_chosen:
        print('you have already selected that letter')
        continue
  
    letters_chosen.append(user_choice)
    if user_choice in chosen_word:
        print('correct')
    else:
        print('incorrect')
        counter-=1

    allLetters = True
    for letter in chosen_word:
        if letter in letters_chosen:
            print(letter, end=" ")
        else:
            print("_", end=" ")
            allLetters = False
    print()

    if allLetters:
        print(f"You won with {counter} lives left!")
        break

    if counter <= 0:
        print(f"You ran out of lives! The answer was {chosen_word}")
        break
    else:
        print(f"Only {counter} lives left")
