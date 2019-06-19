# Class and Constructor
class User:
  def __init__(self, name):
    self.name = name

# Instance
user = User("Ryoko")
print(user.name)

# Method
class User2:
  def say(self, name):
    print("Hello " + name)

# Use method
user = User2()
user.say("Ryoko")
