import random

bingo = []

def format():
  for row in bingo:
    print(row)

def randomnum():
  random_num = random.randint(0,90)
  return random_num

numbers = []

for i in range(8):
  numbers.append(randomnum())

  numbers.sort()

bingo = bingo = [ [ numbers[0], numbers[1], numbers[2]],
          [ numbers[3], "BINGO", numbers[4] ],
          [ numbers [5], numbers[6], numbers[7]]
        ]

format()