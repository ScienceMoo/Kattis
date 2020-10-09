import sys


# check if the pixel is within range
def is_safe(i, j, h, w):
	if (0 <= i) and (i < h) and (0 <= j) and (j < w):
		return True
	else:
		return False


# explore a star
def explore(g, i, j, explored, h, w):

	# Indeces of the neighbours
	row = [-1, 0, 0, 1];
	col = [0, 1, -1, 0];

	# Mark the pixel as explored
	explored[i][j] = True

	# Repeat for neighbours if they are part of the star
	if graph[i][j] == '-':
		for k in range(4):
			if is_safe(i + row[k], j + col[k], h, w):
				if not explored[i + row[k]][j + col[k]]:
					explore(g, i + row[k], j + col[k], explored, h, w)


def count_stars(g, h, w):
	# Intialize all pixels as False
	explored = [[False for j in range(w)] for i in range(h)]

	count = 0
	for i in range(h):
		for j in range(w):
			# If we encounter a new star that hasn't been explored yet, explore it
			if (not explored[i][j]) and g[i][j] == '-':
				# Explore the entire star and add to the star count
				explore(g, i, j, explored, h, w)
				count += 1
			elif not explored[i][j]:
				explored[i][j] = True

	return count


# get lines and remove newline character
lines = list(map(str.rstrip, sys.stdin))

index = 0
case = 1

while index < len(lines):
	line = lines[index]

	size = line.split(" ")

	# initialize the graph
	height = int(size[0])
	width = int(size[1])
	graph = []

	for l in range(height):
		index += 1
		if index < len(lines):
			line = lines[index]
			graph.append([char for char in line])

	actualHeight = len(graph)
	actualWidth = 0
	if actualHeight != 0:
		actualWidth = len(graph[0])

	if actualWidth > 0:
		print("Case " + str(case) + ": " + str(count_stars(graph, actualHeight, actualWidth)))
	else:
		print("Case " + str(case) + ": 0")

	index += 1
	case += 1
