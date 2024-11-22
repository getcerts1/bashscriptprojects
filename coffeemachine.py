""""import modules"""
import os
import time
from inventory import ingredients
from inventory import coins

""""create functions for repeatability"""
def report():
  for key, value in ingredients.items():
    output = f'{key}: {value}'
    print(output)

"""" Prompt user by asking beverage
This should be in a loop once drink is dispensed"""
space = f'\n' * 5
os.system('clear')

accepted_coins = [1,5,10,25]


while True:
  
  beverages = input(f'espresso/latte/cappuccino: {space} ').lower()

  if beverages == 'espresso':
    if ingredients["water"] >= 50 and ingredients["coffee"] >= 18:
      ingredients["water"] -= 50 
      ingredients["coffee"] -= 18

      total = {
        "penny": 0,
        "nickel": 0,
        "dime": 0,
        "quarter": 0
      }

      def count_total(total):
        return total['penny'] * 1 + total['nickel'] + total['dime'] + total['quarter']
      
      def subtract_from_register():
        coins['penny']-=total['penny']
        coins["nickel"]-=total['nickel']
        coins['dime']-=total['dime']
        coins['quarter']-=total['quarter']



      
      print('the price is $1.50')
      while count_total(total) < 150:
        coins_input = int(input('enter coins: '))

        if coins_input == "":  # Allow empty input to continue
          print("Please insert a valid coin")
          continue
        

        if coins_input in accepted_coins:
          if coins_input == 1:
            total['penny'] += 1
          elif coins_input == 5:
            total['nickel'] += 5
          elif coins_input == 10:
            total['dime'] += 10
          else:
            total['quarter'] += 25
          print(f"Current total: {count_total(total)} cents")
          print(f'there is ${(150 - count_total(total)) / 100} left')
        else:
          print('please insert a valid coin')
    
      subtract_from_register()
        
    else:
      print('not enough ingredients in the machine')
      break
  
  elif beverages == 'latte':
    if ingredients["water"] >= 200 and ingredients["coffee"] >= 24 and ingredients["milk"] >= 150:
      ingredients["water"] -= 200 
      ingredients["coffee"] -= 25
      ingredients["milk"] -150

      total = {
        "penny": 0,
        "nickel": 0,
        "dime": 0,
        "quarter": 0
      }

      def count_total(total):
        return total['penny'] * 1 + total['nickel'] + total['dime'] + total['quarter']
      
      def subtract_from_register():
        coins['penny']-=total['penny']
        coins["nickel"]-=total['nickel']
        coins['dime']-=total['dime']
        coins['quarter']-=total['quarter']


      print('The price is $2.50')
      while count_total(total) < 250: 
        coins_input = int(input('enter coins: '))

        if coins_input == "":  # Allow empty input to continue
          print("Please insert a valid coin")
          continue
        

        if coins_input in accepted_coins:
          if coins_input == 1:
            total['penny'] += 1
          elif coins_input == 5:
            total['nickel'] += 5
          elif coins_input == 10:
            total['dime'] += 10
          else:
            total['quarter'] += 25
          print(f"Current total: {count_total(total)} cents")
          print(f'there is ${(250 - count_total(total)) / 100} left')
        else:
          print('please insert a valid coin')
    
      subtract_from_register()
        
    else:
      print('not enough ingredients in the machine')
      break
  
  elif beverages == 'cappuccino':
    if ingredients["water"] >= 250 and ingredients["coffee"] >= 24 and ingredients["milk"] >= 100:
      ingredients["water"] -= 250 
      ingredients["coffee"] -= 24
      ingredients["milk"] -100

      total = {
        "penny": 0,
        "nickel": 0,
        "dime": 0,
        "quarter": 0
      }

      def count_total(total):
        return total['penny'] * 1 + total['nickel'] + total['dime'] + total['quarter']
      
      def subtract_from_register():
        coins['penny']-=total['penny']
        coins["nickel"]-=total['nickel']
        coins['dime']-=total['dime']
        coins['quarter']-=total['quarter']



      print('the price is $3.00')
      while count_total(total) < 300:
        coins_input = int(input('enter coins: '))

        if coins_input == "":  # Allow empty input to continue
          print("Please insert a valid coin")
          continue
        

        if coins_input in accepted_coins:
          if coins_input == 1:
            total['penny'] += 1
          elif coins_input == 5:
            total['nickel'] += 5
          elif coins_input == 10:
            total['dime'] += 10
          else:
            total['quarter'] += 25
          print(f"Current total: {count_total(total)} cents")
          print(f'there is ${(250 - count_total(total)) / 100} left')
        else:
          print('please insert a valid coin')
    
      subtract_from_register()
        
    else:
      print('not enough ingredients in the machine')
      break
  #entering report displays the remaining ingredients"""
  elif beverages == 'report':
    os.system('clear')
    report()
    time.sleep(5)
    os.system('clear')
    
  #turn off machine using off - this breaks out of loop and ends machine usage
  elif beverages == 'off':
    break




