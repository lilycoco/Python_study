# タプルはイミュータブルなデータ構造

# Create
nums = "One", "Two", "Three"
nums = ("One", "Two", "Three")

# Immutable
# nums[0] = "Zero" # => Error!

# Get 
nums[0]
for n in nums:
  print(n)

# Assign
a, b, c = nums
print(a)
