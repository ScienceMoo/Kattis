import sys

# get lines and remove newline character
lines = list(map(str.rstrip, sys.stdin))

index = 2
case = 0

while index < len(lines):
	case += 1
	vector1 = list(map(int, lines[index].split()))
	vector2 = list(map(int, lines[index+1].split()))

	# sort them in opposite order so that the lowest get multiplied by the highest
	vector1.sort()
	vector2.sort(reverse=True)

	sum = 0
	for i in range(len(vector1)):
		sum += vector1[i] * vector2[i]

	print("Case #" + str(case) + ": " + str(sum))
	index += 3
