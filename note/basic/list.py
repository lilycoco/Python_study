# リスト型は配列形式でデータを保持する

# Create
users = ["Yo", "Ken", "Nao", "Shin", "Lee"]

# Add
users.append("Miu")

# Delete
users.remove("Nao")

# Index access
users[0] # => Yo
users[0:2] # => ['Yo', 'Ken']
users[1:] # => ['Ken', 'Shin', 'Lee', 'Miu']
users[::2] # => ['Yo', 'Shin', 'Miu']
users[::-1] # => ['Miu', 'Lee', 'Shin', 'Ken', 'Yo']
print(users[::-1])


# list comprehension
users = [u.lower() for u in users if u.find("e") != -1] # => ['ken', 'lee']
print(users)