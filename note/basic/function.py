# Basic
def add(a, b):
  return a + b
result = add(10, 20)
print(result)

# Keywoed arguments
def create_date(
  year=0, month=0, date=0
): return "..."
result = create_date(year=2017, date=10)
print(result)

# Argment default value
def pow(a, b=2):
  return a ** b
result = pow(10)
print(result)

# Multiple return 
def get_user():
  return 'Yohei', 30
name, age = get_user()
print(name)