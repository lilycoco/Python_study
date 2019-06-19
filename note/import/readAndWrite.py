# ファイルの読み書き

# Write a file
f = open("python.txt", "w")
f.write("Hello")
f.close()

# Append a file
f = open("python.txt", "a")
f.write("Hi")
f.close()

# Read a file
f = open ("python.txt")
txt = f.read()
f.close()

# using With
with open("python.txt") as f:
  txt = f.read()

  