import sys


# just check all permutations
def find_closest_sum(old_numbers, query):
	new_numbers = []

	smallest_dif = abs(old_numbers[0] + old_numbers[1] - query)
	best = [0, 1]
	total = old_numbers[0] + old_numbers[1]

	for x in range(len(old_numbers)):
		new_numbers.append(old_numbers[x])

	index = 0

	while len(new_numbers) > 1:
		for k in range(1, len(new_numbers)):
			current = abs(new_numbers[0] + new_numbers[k] - query)
			if current < smallest_dif:
				smallest_dif = current
				total = new_numbers[0] + new_numbers[k]
				best[0] = index
				best[1] = i
		new_numbers.pop(0)
		index += 1

	return total

# get lines and remove newline character
lines = list(map(str.rstrip, sys.stdin))

index = 0
case = 1

while index < len(lines):
	numbers = []

	n = int(lines[index])

	for i in range(n):
		index += 1
		numbers.append(int(lines[index]))

	index += 1

	print("Case " + str(case) + ":")

	m = int(lines[index])
	for i in range(m):
		index += 1

		result = find_closest_sum(numbers, int(lines[index]))

		print("Closest sum to " + str(lines[index]) + " is " + str(result) + ".")

	index += 1
	case += 1
