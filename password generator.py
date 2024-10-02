import random
import string

name = input('what is your name? ')
letters = int(input('how many letters would you like? '))
symbols = int(input('how many symbols would you like? '))
numbers = int(input('how many numbers would you like? '))
total = letters + symbols + numbers


random_char = []

for i in range(1, letters + 1):
  random_char.append(random.choice(string.ascii_lowercase))

for i in range(1, symbols + 1):
  random_char.append(random.choice(string.punctuation))

for i in range(1, numbers + 1):
  random_char.append(random.choice(string.digits))

random.shuffle(random_char)
password = ''.join(random_char)

print(f'your password is -- {password} -- don\'t forget to change it after three months {name}')



