T = int(input())

for _ in range(T):
	n = int(input())
	cities = {}

	for i in range(n):
		city = input()
		cities[city] = 1

	print(len(cities))