# 条件分岐

hour = 11
day_of_week = "Sunday"

if hour <= 6:
  print("so sleepy")

elif 10 <= hour <= 12:
  print("good morning")

elif hour < 12 and day_of_week == "Sunday" or hour > 20:
  pass

else:
  print("hi")