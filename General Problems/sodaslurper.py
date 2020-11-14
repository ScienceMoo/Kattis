e, f, c = list(map(int, input().split()))

bottles = e + f
drinks = 0

while bottles >= c:
	bottles -= c
	bottles += 1
	drinks += 1

print(drinks)

