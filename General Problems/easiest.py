n = int(input())

while not n == 0:
	ndigits = [int(c) for c in str(n)]
	total = sum(ndigits)
	p = 11
	np = n * p
	npdigits = [int(c) for c in str(np)]
	while not sum(npdigits) == total:
		p += 1
		np = n * p
		npdigits = [int(c) for c in str(np)]

	print(p)

	n = int(input())