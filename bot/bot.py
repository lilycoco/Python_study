from def_heisei import heisei_command
from def_random import choice_command, dice_command
from def_datetime import today_command, now_command, weekday_command

command_file = open('bot.txt', encoding='utf-8')
raw_data = command_file.read()
command_file.close()
lines = raw_data.splitlines()

bot_dict = {}
for line in lines:
  word_list = line.split(',')
  key = word_list[0]
  response = word_list[1]
  bot_dict[key] = response

while True:
  command = input('bot> ')
  response = ''
  try:
    for msg in bot_dict:
      if msg in command:
        response = bot_dict[msg]
        break

    if 'heisei' in command:
      response = heisei_command(command)

    if 'eto' in command:
      response = eto_command(command)

    if 'choice' in command:
      response = choice_command(command)

    if 'dice' in command:
      response = dice_command()

    if 'today' in command:
      response = today_command()

    if 'now' in command:
      response = now_command()

    if 'weekday' in command:
      response = weekday_command(command)

    if not response:
      response = 'What??'

    print(response)
    
    if 'さよなら' in command:
      break

  except Exception as e:
      print('unexpexted error')
      print('* errot type:', type(e))
      print('* detail:', e)

