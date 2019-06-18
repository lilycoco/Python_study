# セット型は重複が無く、順序を持たないデータの集合

# Create
set_ = {
  "Tennis", 
  "Ramen",
  "Programming"
}

# Add / Delete
set_.add("Gs")
set_.remove("Ramen")

# Get
# set_[0] # => Error!!

for s in set_:
  print(s)

# Calc
set1 = set([1, 2, 3, 4, 5])
set2 = set([3, 4, 5])
print(set1 - set2)