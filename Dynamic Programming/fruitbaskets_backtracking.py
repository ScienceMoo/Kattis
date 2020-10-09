import sys


class Backtracking:

	def __init__(self):
		self.backtrack_sum = 0

	# backtracking search to eliminate baskets that are too small
	def eliminate_baskets(self, basket_weight_so_far, index, fruit_array, num_fruits):
		if basket_weight_so_far >= 200:
			return

		if index >= num_fruits:
			self.backtrack_sum += basket_weight_so_far
			return

		self.eliminate_baskets(basket_weight_so_far, index + 1, fruit_array, num_fruits)
		self.eliminate_baskets(basket_weight_so_far + fruit_array[index], index + 1, fruit_array, num_fruits)


# get lines and remove newline character
lines = list(map(str.rstrip, sys.stdin))

# get fruits and the sum of their weights
arr = lines[1].split(" ")
fruits = []
sum = 0
for f in arr:
	f_int = int(f)
	sum += f_int
	fruits.append(f_int)

# total weight of all possible baskets
total = (2 ** (len(fruits) - 1)) * sum

# subtract weight of all baskets less than 200
if len(fruits) > 0:
	thing = Backtracking()
	thing.eliminate_baskets(0, 0, fruits, len(fruits))
	print(total - thing.backtrack_sum)