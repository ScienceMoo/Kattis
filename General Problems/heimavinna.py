numbers = input().split(";")
count = 0
for number in numbers:
	if "-" in number:
		a, b = map(int, number.split("-"))
		count += b - a + 1
	else:
		count += 1

print(count)