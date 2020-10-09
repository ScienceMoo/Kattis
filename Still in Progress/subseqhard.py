import sys

def seq(nums, c, i):
	while (c != 47) and (i < len(nums)):
		c += nums[i]
		if c == 47:
			return [True, c, i]
		i += 1
	return [False, c, i]


# get lines and remove newline character
lines = list(map(str.rstrip, sys.stdin))

index = 2

while index < len(lines):
	line = lines[index]

	index += 1
	numbers = list(map(int, lines[index].split(" ")))

	count = 0
	c = 0
	i = 0
	while numbers:
		max_remaining = (len(numbers) - 1) * 20000
		if abs(numbers[0]) - max_remaining < 48:
			res, c, i = seq(numbers, c, i)
			if res:
				count += 1
				c -= numbers.pop(0)
			else:
				numbers.pop(0)
				c = 0
				i = 0
		else:
			numbers.pop(0)

	print(count)
	index += 2
