n = int(input())
upper = float("inf")
lower = -float("inf")

while not n == 0:
	result = input()

	while not result == "right on":
		if result == "too high":
			if n < upper:
				upper = n
		elif result == "too low":
			if n > lower:
				lower = n
		n = int(input())
		result = input()

	if result == "right on":
		if lower < n < upper:
			print("Stan may be honest")
		else:
			print("Stan is dishonest")

	n = int(input())
	upper = float("inf")
	lower = -float("inf")

