import sys

# get lines and remove newline character
lines = list(map(str.rstrip, sys.stdin))

number = int(lines[0])

index = 2

while index < len(lines):
	distances = list(map(int, lines[index].split()))
	largest_distance = max(distances)
	maximum_distance = sum(distances)
	largest_distance += maximum_distance + 1

	positions = [[maximum_distance for _ in range(largest_distance)] for _ in range(len(distances) + 1)]
	directions = [[0 for _ in range(largest_distance)] for _ in range(len(distances) + 1)]
	positions[0][0] = 0

	for i in range(len(distances)):
		for d in range(maximum_distance + 1):
			current_max = positions[i][d]
			up = d + distances[i]
			down = d - distances[i]

			if positions[i + 1][up] > max(up, current_max):
				# going up so increase the current_max if necessary
				positions[i + 1][up] = max(up, current_max)
				directions[i + 1][up] = 1

			# this will only happen when i > 0
			if down >= 0 and positions[i + 1][down] > current_max:
				# going down so keep the same current max
				positions[i + 1][down] = current_max
				directions[i + 1][down] = -1

	result = []
	height = positions[len(distances)][0]
	if height < maximum_distance:
		distance = 0
		for x in range(len(distances)):
			if directions[len(distances) - x][distance] == 1:
				distance -= distances[len(distances) - x - 1]
				result.insert(0, "U")
			else:
				distance += distances[len(distances) - x - 1]
				result.insert(0, "D")
		print("".join(result))
	else:
		print("IMPOSSIBLE")
	index += 2