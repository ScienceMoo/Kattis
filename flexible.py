w, _ = map(int, input().split())

partitions = list(map(int, input().split()))

possible_widths = []

previous = []

for p in partitions:
	if not p in possible_widths:
		possible_widths.append(p)
	if not (w - p) in possible_widths:
		possible_widths.append(w - p)
	for thing in previous:
		if not (p - thing) in possible_widths:
			possible_widths.append(p - thing)

	previous.append(p)
	possible_widths = sorted(possible_widths)

for thing in possible_widths:
	print(thing, end=" ")

print(w)

