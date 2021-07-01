y = int(input())

x = 2018
month = 3

while x < 10001:
    if x == y:
        print("yes")
        break
    elif x > y:
        print("no")
        break
    x += 2
    month += 2
    if month > 11:
        x += 1
        month = month % 12