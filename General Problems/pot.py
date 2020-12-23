n = int(input())

sum = 0

for _ in range(n):
	number = input()
	sum += int(number[:-1]) ** int(number[-1])

print(sum)