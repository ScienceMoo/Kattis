

# basic Fenwick as described on Wikipedia
class FenwickTree:
	def __init__(self, arr):
		# initialize the tree with enough space for the books and requests
		self.n = len(arr)
		self.sum_tree = [0] * (self.n + 1)
		for i, x in enumerate(arr):
			self.update(i + 1, x)

	def update(self, i, value):
		while i <= self.n:
			self.sum_tree[i] += value
			i += i & (-i)

	def sum(self, i):
		sum = 0
		while i > 0:
			sum += self.sum_tree[i]
			i -= i & (-i)
		return sum


def move_top(i, movie, r, ft, index):
	c = ft.sum(index[movie]) - 1

	# all the movies have value of 1
	ft.update(index[movie], -1)

	# place at the top, leaving room for more requests
	index[movie] = r - i
	ft.update(index[movie], 1)
	return f'{c}'


N = int(input())

# for each test case
for _ in range(N):
	m, r = map(int, input().split())
	requests = list(map(int, input().split()))

	ft = FenwickTree([0] * r + [1] * m)
	# Initialize indexes in increasing order
	index = [0] + [r + i + 1 for i in range(m)]

	result = []
	for i, x in enumerate(requests):
		result.append(move_top(i, x, r, ft, index))

	print(' '.join(result))