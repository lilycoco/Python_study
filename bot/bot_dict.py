# count = 10
# while count > 0:
#   print(count)
#   count = count - 1
# print('終了する')

bot_dict = {
  'Hello': 'HELLOW',
  'Thanks': 'THANKS',
  'Bye': 'BYE',
}
while True:
  command = input('bot> ')
  response = ''
  for msg in bot_dict:
    if msg in command:
      response = bot_dict[msg]
      break

  if not response:
    response = 'What??'
  print(response)
  
  if 'bye' in command:
    break


  # if 'Hi' in command:
  #   print('How are you?')
  # elif 'Thanks' in command:
  #   print('No worries')
  # elif 'bye' in command:
  #   break
  # else:
  #   print('What??')
