def heisei_command(command):  
  heisei, year_str = command.split()
  year = int(year_str)
  if year >= 1989:
    heisei_year = year -1988
    response = '西暦{}年は、{}{}年です。'.format(year, heisei, heisei_year)
  else:
    response = '西暦{}年は、平成じゃない'.format(year)
  return response
