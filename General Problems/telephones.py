import sys

# get lines and remove newline character
lines = list(map(str.rstrip, sys.stdin))

index = -1

while index < len(lines) - 1:
	index += 1
	first_line = list(map(int, lines[index].split()))
	num_calls = first_line[0]
	num_intervals = first_line[1]

	bins = [0] * num_intervals
	calls = []

	for _ in range(num_calls):
		index += 1
		call = list(map(int, lines[index].split()))
		calls.append(call)

	for _ in range(num_intervals):
		index += 1
		interval = list(map(int, lines[index].split()))
		start = interval[0]
		end = interval[0] + interval[1]
		sum = 0
		for call in calls:
			call_start = call[2]
			call_end = call[2] + call[3]
			if (call_start < end and call_end > start):
				sum += 1
		print(sum)