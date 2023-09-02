import random

num_of_digits = int(input('select a number of digits for your password: > '))
pin = ""
for i in range(num_of_digits):
    password = str(random.randint(1,9))
    pin+=password
    
print(pin)

