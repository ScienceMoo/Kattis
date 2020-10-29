import sys

# get lines and remove newline character
lines = list(map(str.rstrip, sys.stdin))

index = 1
while index < len(lines):
	first_line = list(map(int, lines[index].split()))
	index += 1

	stack = []
	visited = [False] * (first_line[0] + 1)
	collisions = [[] for _ in range(first_line[0] + 1)]

	for _ in range(first_line[1]):
		line = list(map(int, lines[index].split()))
		index += 1
		collisions[line[0]].append(line[1])

	for _ in range(first_line[2]):
		line = int(lines[index])
		index += 1
		stack.append(line)

	sum = 0
	while len(stack) > 0:
		current = stack.pop(0)
		if not visited[current]:
			visited[current] = True
			sum += 1
			for target in collisions[current]:
				stack.append(target)

	print(sum)
