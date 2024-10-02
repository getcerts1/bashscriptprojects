numofingredients = int(input('How many ingredients would you like to add to your basket? '))
ingredients = []

for i in range(numofingredients):
    userinput = input(f'Ingredient {i + 1}: ')

    
    if userinput.isdigit():
        print('Please enter a word, not a number.')
    
        while userinput.isdigit():
            userinput = input(f'Ingredient {i + 1}: ')
    
    ingredients.append(userinput)

print(ingredients)
