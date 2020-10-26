import sys

# get lines and remove newline character
lines = list(map(str.rstrip, sys.stdin))

number = int(lines[0])

index = 2


def find_min(current_height, max_height, numbers, sequence):
	if len(numbers) == 1:
		if current_height - numbers[0] != 0:
			return [1001, sequence]
		else:
			return [max_height, sequence + "D"]
	elif current_height < 0:
		return [1001, sequence]
	else:
		new_max = max_height
		if current_height + numbers[0] > max_height:
			new_max = current_height + numbers[0]

		add_result = find_min(current_height - numbers[0], max_height, numbers[1:], sequence + "D")
		minus_result = find_min(current_height + numbers[0], new_max, numbers[1:], sequence + "U")
		if add_result[0] < minus_result[0]:
			return add_result
		else:
			return minus_result

# initialize the first digit using numbers 1-9
while index < len(lines):
	distances = list(map(int, lines[index].split()))

	result = find_min(0, 0, distances, "")

	if result[0] < 1001:
		print(result[1])
	else:
		print("IMPOSSIBLE")

	index += 2