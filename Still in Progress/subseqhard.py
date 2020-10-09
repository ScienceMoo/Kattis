import sys


class BinarySearchTree:
	def __init__(self, array, length):
		self.array = array
		self.length = length
		self.count = 0

	def my_genius_algorithm(self):
		if self.length <= 0:
			return

		# initialize array
		current_seq = []
		current_sum = 0

		# take first number
		first = self.array[0]
		current_seq.append(first)
		current_sum += first
		if first == 47:
			self.count += 1

		if self.length > 1:
			self.add_to_end(current_sum, current_seq, 1)

	def add_to_end(self, current_sum, current_seq, i):
		new_seq = current_seq[:]
		current = self.array[i]
		new_seq.append(current)
		new_sum = current_sum + current
		if new_sum == 47:
			self.count += 1

		if i + 1 < self.length:
			self.add_to_end(new_sum, new_seq, i+1)

		self.remove_from_start(new_sum, new_seq)

	def remove_from_start(self, current_sum, current_seq):
		new_seq = current_seq.copy()
		current = new_seq.pop(0)

		new_sum = current_sum - current
		if new_sum == 47:
			self.count += 1

		if len(new_seq) > 1:
			self.remove_from_start(new_sum, new_seq)


# get lines and remove newline character
lines = list(map(str.rstrip, sys.stdin))

index = 2

while index < len(lines):
	num_numbers = int(lines[index])

	index += 1
	if num_numbers > 0:
		numbers = list(map(int, lines[index].split(" ")))

		tree = BinarySearchTree(numbers, num_numbers)
		tree.my_genius_algorithm()

		print(tree.count)
	else:
		print(0)
	index += 2
