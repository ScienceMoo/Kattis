import math
s = input()

l = len(s)

unique = []
for char in s:
  if char not in unique:
      unique.append(char)
  else:
    unique.remove(char)

num_unique = len(unique) - 1

if num_unique < 0:
	num_unique = 0

print(num_unique)

