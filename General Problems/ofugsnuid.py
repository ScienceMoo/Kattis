N = int(input())

numbers = []

for _ in range(N):
	numbers.append(input())

for _ in range(N):
	print(numbers.pop())