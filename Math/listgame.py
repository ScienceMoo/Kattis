import math
X = int(input())
y = X

count = 0
div = 2

while ((div ** 2) <= X) and y > 1:
    while y % div == 0:
        y = y / div
        count += 1
    div += 1
if y > 1:
    count += 1
        
print(count)