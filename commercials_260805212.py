import sys


# Look for continuous subarray with largest profit
def max_subarray(num_students_per_break, p):
	best_sum = 0 # because anything less than 0 is not profit
	current_sum = 0
	for x in num_students_per_break:
		# if adding this number will result in overall profit then keep it
		# otherwise, restart sum at 0
		current_sum = max(0, current_sum + x - p)
		best_sum = max(best_sum, current_sum)
	return best_sum


# get lines and remove newline character
lines = list(map(str.rstrip, sys.stdin))

firstLine = lines[0].split()
price = int(firstLine[1])
num_students = list(map(int, lines[1].split()))

print(max_subarray(num_students, price))
