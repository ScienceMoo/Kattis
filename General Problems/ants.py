num_tests = int(input())

for _ in range(num_tests):
	l, n = map(int, input().split())

	ants = []
	while len(ants) < n:
		ants += list(map(int, input().split()))

	min_time = 0

	# min time is the farthest distance of an ant from the end of the stick
	for ant in ants:
		min_time = max(min(ant, l - ant), min_time)

	ants = sorted(ants)

	# max time depends on the outermost ants
	max_time = [ants[0], ants[n - 1], l - ants[0], l - ants[n - 1]]

	print(str(min_time) + " " + str(max(max_time)))