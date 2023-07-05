import random
import os
import time

def rolldice(sides):
  num_rolled = random.randint(1, sides)
  return num_rolled

def char_health():
  health = (rolldice(6) * rolldice(12) / 12) + 10
  return int(health)

def char_strength():
  strength = (rolldice(6) * rolldice(12)) + 12
  return int(strength)


character_1_health = char_health()
character_2_health = char_health()
character_1_strength = char_strength()
character_2_strength = char_strength()

print('⚔️ BATTLE TIME ⚔️')
print()
character_1_name = input('Name your Legend: ')
print(character_1_name)
character_1_type = input('Character type: ')
print(character_1_type)

print(character_1_name)
print('HEALTH:', character_1_health)
print('STRENGTH:', character_1_strength)
print()
print()

print('Who are they battling?')
time.sleep(1)

character_2_name = input('Name your Legend: ')
print(character_2_name)
character_2_type = input('Character type: ')
print(character_2_type)

print(character_2_name)
print('HEALTH:', character_2_health)
print('STRENGTH:', character_2_strength)

  
print('⚔️ BATTLE TIME ⚔️')
os.system("clear")


round = 1

while True:
  time.sleep(1)
  os.system("clear")
  print("⚔️ BATTLE TIME ⚔️")
  print()
  print("The battle begins!")
  roll_for_char_1 = rolldice(6)
  roll_for_char_2 = rolldice(6)
  difference = abs(character_1_strength - character_2_strength) + 1
  if roll_for_char_1 > roll_for_char_2:
    character_2_health -= difference
    if round==1:
      print(character_1_name, "wins the first blow")
    else:
      print(character_1_name, "wins round", round)
  elif roll_for_char_2 > roll_for_char_1:
    character_1_health -= difference
    if round==1:
      print(character_2_name, "wins the first blow")
    else:
      print(character_2_name, "wins round", round)
  else:
    print("Their swords clash and they draw round", round)
  print()
  print(character_1_name)
  print("HEALTH:", character_1_health)
  print()
  print(character_2_name)
  print("HEALTH:", character_2_health)
  print()
  if character_1_health<=0:
    print(character_1_name, "has died!")
    winner = character_2_name
    break
  elif character_2_health<=0:
    print(character_2_name, "has died!")
    winner = character_1_name
    break
  else:
    print("And they're both standing for the next round")
    round += 1
    
time.sleep(1)
os.system("clear")
print("⚔️ BATTLE TIME ⚔️")
print()
print(winner, "has won in", round, "rounds")
    
    
 