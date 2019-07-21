year_str = input('生まれ年は？: ')
year = int(year_str)
number_of_eto = (year + 8) % 12
eto_list = ['子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥']
print('あなたの干支は{}です' .format(eto_list[number_of_eto]))
