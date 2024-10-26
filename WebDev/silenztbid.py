import os


print('Welcome to the secret auction program')
num_of_bidders = int(input('how many bidders are present? '))

record = {}

for i in range(num_of_bidders):
    nameinput = input('What is your name? ')
    bid = int(input('What is your bid?: $'))

    record[nameinput] = bid 
    os.system('clear')

  


highest_bidder = max(record, key=record.get)
highest_bid = record[highest_bidder]

print(f'The highest bidder is {highest_bidder} with a bid of ${highest_bid}')


