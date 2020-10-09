import sys


# recursive search for lucky numbers
def search_for_lucky(num_so_far, digit, max):
	c = 0

	# find all the next digits using numbers 0-9
	for x in range(10):
		new_number = num_so_far + str(x)
		if int(new_number) % digit == 0:
			if digit == max:
				c += 1
			else:
				c += search_for_lucky(new_number, digit + 1, max)

	return c


# get lines and remove newline character
lines = list(map(str.rstrip, sys.stdin))

# get the number of digits
n = int(lines[0])

count = 0

# initialize the first digit using numbers 1-9
for num in range(1, 10):
	newNumber = str(num)
	count += search_for_lucky(newNumber, 2, n)

print(count)
