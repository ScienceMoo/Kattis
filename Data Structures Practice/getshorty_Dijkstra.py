import math

class Graph:
	def __init__(self, n, m):
		self.edges = [[-1 for _ in range(n)] for _ in range(n)]
		for _ in range(m):
			x, y, f = input().split()
			self.edges[int(x)][int(y)] = float(f)
			self.edges[int(y)][int(x)] = float(f)

# get first test case
n, m = map(int, input().split())

while not n == 0:
	visited = [False] * n
	remaining = set(range(0, n))

	shortness = [-float('inf')] * n

	# he starts at full height
	shortness[0] = 0
	i = 0
	visited[i] = 0

	graph = Graph(n, m)

	# adjusted the Dijkstra algorithm because we only need 1 path
	while not visited[n-1]:
		remaining.remove(i)
		best = -float('inf')
		next = -1
		for j in remaining:
			if graph.edges[i][j] > 0:
				shortness[j] = shortness[i] + math.log(graph.edges[i][j])
			elif graph.edges[i][j] == 0:
				shortness[j] = -float('inf')
			if shortness[j] >= best:
				best = shortness[j]
				next = j
		# continue path along best route
		i = next
		visited[i] = True

	print("{:.4f}".format(math.exp(shortness[n-1])))

	# next test case
	n, m = map(int, input().split())