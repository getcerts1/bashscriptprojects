import os

def calculator():
    while True:
        num1 = float(input('Enter a value: '))
        
        while True:
            
            symbols = {
                "+": "addition",
                "-": "subtraction",
                "x": "multiplication",
                "/": "division"
            }
            
            num2 = float(input('Enter another value: '))
            
        
            print(f"Available operations: {', '.join(symbols.keys())}")
            
            symbol = input('Choose a symbol: ')

            if symbol == '+':
                answer = num1 + num2
            elif symbol == '-':
                answer = num1 - num2
            elif symbol == 'x':
                answer = num1 * num2
            elif symbol == '/':
                if num2 == 0:
                    print("Cannot divide by zero.")
                    continue
                answer = num1 / num2
            else:
                print("Invalid symbol, please try again.")
                continue  # Re-prompt if an invalid symbol is entered

            # Format the answer
            if answer % 1 == 0:
                answer = int(answer)
            else:
                answer = round(answer, 2)

            print(f"The answer is: {answer}")

            # Option to continue with the current answer
            restart_decision = input(f"Type 'y' to continue with {answer} or 'n' to start a new calculation: ")
            
            if restart_decision.lower() == 'y':
                num1 = answer
                os.system('clear') 
            else:
                break  # Break out of the inner loop to start a new calculation
        
      
        new_calculation = input("Would you like to start a new calculation? (yes/no): ")
        if new_calculation.lower() != 'yes':
            break  





def fridge():
    fridge = []

    while True:
        check_content = input('Would you like to view the contents of the fridge? (yes/no): ').lower()
        if check_content == 'yes':
            print(fridge)
        else:
            add_content = input('Would you like to add items to the fridge? (yes/no): ').lower()
            if add_content == 'yes':
                items_to_add = input('Add item: ')
                fridge.append(items_to_add)
            should_exit = input('Would you like to leave the fridge? (yes/no): ').lower()
            if should_exit == 'yes':
                break

while True:
    appliance_select = input('Welcome to our house, what appliance do you want to use? (calculator/fridge): ').lower()

    if appliance_select in ['calculator', 'calc']:
        print(calculator())
    elif appliance_select == 'fridge':
        fridge()
    else:
        should_exit = input('Would you like to exit the household? (yes/no): ').lower()
        if should_exit == 'yes':
            break
