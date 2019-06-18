# 辞書型はkey-valueで値を保持する

# Create
user_dict = {
  "Yohei": 30,
  "John": 35
}

# Get
user_dict["Yohei"]
user_dict.get("Nao", 20)

# Update / Delete
user_dict["Yohei"] = 31
del user_dict["John"]

# Get all
for k, v in user_dict.items():
  print(k, v)
