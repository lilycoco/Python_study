def eto_command(command):
  eto, year = command.split()
  eto_list = ['子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥']
  eto_number = (year + 8) % 12
  response = print('{}年生まれの干支は{}です' .format(year, eto_list[eto_number]))
  return response