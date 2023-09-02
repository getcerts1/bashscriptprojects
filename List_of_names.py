import time, os

Title = 'Names list'
print(f'{Title:>30}')

list_of_names =[]
new_version_list = []

def prettyprint():
  for item in list_of_names:
      print()
      print(item)
  time.sleep(2)
  os.system('clear')
  
def new_version_list_printed():
  for item in new_version_list:
      print()
      print(item)
  time.sleep(2)
  os.system('clear')

while True:
  first_name = input('first name > ').strip().capitalize()
  if first_name not in list_of_names:
    list_of_names.append(first_name)
  elif first_name in list_of_names:
    print('this first name already exists in the list')
  prettyprint()
  last_name = input('last name > ').strip().capitalize()
  if last_name not in list_of_names:
    list_of_names.append(last_name)
  elif last_name in list_of_names:
    print('this last name already exists in the list')
  prettyprint()

  full_name = f'{first_name} {last_name}'
  new_version_list.append(full_name)
  new_version_list_printed()

