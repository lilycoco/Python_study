from datetime import date, datetime

def today_command():
  today = date.today()
  response = 'today is {}'.format(today)
  return response

def now_command():
  now = datetime.now()
  response = '{} now'.format(now)
  return response

def weekday_command(command):
  data = command.split()
  year = int(data[1])
  month = int(data[2])
  day = int(data[3])
  one_day = date(year, month, day)

  weekday_str = '月火水木金土日'
  weekday = weekday_str[one_day.weekday()]

  response = '{} is {}'.format(one_day, weekday)
  return response

