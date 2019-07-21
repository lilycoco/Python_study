import random

def choice_command(command):
  data = command.split()
  choiced = random.choice(data[1:])
  response = '「{}」'.format(choiced)
  return response

def dice_command():
  num = random.randrange(1, 7)
  response = '「{}」'.format(num)
  return response
