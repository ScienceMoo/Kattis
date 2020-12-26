start, a, b, c = map(int, input().split())

while not (start == 0 and a == 0 and b == 0 and c == 0):
	total = 360 * 3

	if a > start:
		total += (40 + start - a) * 9
	else:
		total += (start - a) * 9

	if b > a:
		total += (b - a) * 9
	else:
		total += (40 + b - a) * 9

	if c > b:
		total += (40 + b - c) * 9
	else:
		total += (b - c) * 9

	print(total)
	start, a, b, c = map(int, input().split())