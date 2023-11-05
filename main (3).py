import random

print('Welcome, Let\'s roll a dice!')
again = True

while again:
  another_roll = input('To roll a dice choose y/n and press enter.\n')
  
  while another_roll.lower() not in ['y', 'n'] :
    another_roll = input('This is not y/n, please chooes y/n.\n')

  if another_roll.lower() == 'y':
    print(random.randint(1,6))
    continue
    
  elif another_roll.lower() == 'n':
    print('Have a nice day. Goodbye!')
    break