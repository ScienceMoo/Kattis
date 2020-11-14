import math
from queue import PriorityQueue

class Graph:
	def __init__(self, n, m):
		self.edges = [[] for _ in range(n)]
		for _ in range(m):
			x, y, f = input().split()
			x = int(x)
			y = int(y)
			f = float(f)
			self.edges[x].append([y, f])
			self.edges[y].append([x, f])

# get first test case
n, m = map(int, input().split())

while not n == 0:
	graph = Graph(n, m)
	visited = set()
	queue = PriorityQueue()

	# he starts at full height
	queue.put((-1 * math.log(1), 0))

	while True:
		if queue.empty():
			raise Exception('no possible moves')
		height, intersection = queue.get()
		visited.add(intersection)
		if intersection == n - 1:
			print("{:.4f}".format(math.exp(-1 * height)))
			break
		for other, multipler in graph.edges[intersection]:
			if other not in visited:
				queue.put((height - math.log(multipler), other))
	n, m = map(int, input().split())

