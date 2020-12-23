num_groups = int(input())

for _ in range(num_groups):
	numbers = list(map(int, input().split()))[1:]
	# print(numbers)

	current = numbers[0]
	idx = 2
	for num in numbers[1:]:
		current += 1
		if not num == current:
			break
		idx += 1

	print(idx)