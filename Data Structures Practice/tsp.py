import math


def dist(pt1, pt2):
	return math.sqrt(((pt1[0] - pt2[0]) ** 2) + ((pt1[1] - pt2[1]) ** 2))


class TSP:
	def __init__(self, n):
		self.order = [0] + [-1] * (n-1)
		self.vertices = []
		self.visited = [True] + [False] * (n-1)

		for k in range(n):
			x, y = map(float, input().split())
			self.vertices.append((x, y))


	# greedy algorithm (naive, not optimal)
	def search(self, start, n):
		if n == len(self.vertices):
			return
		dis = float("inf")
		best = -1
		for i in range(len(self.vertices)):
			if not self.visited[i]:
				d = dist(self.vertices[start], self.vertices[i])
				if d < dis:
					dis = d
					best = i
		self.visited[best] = True
		self.order[best] = n
		self.search(best, n + 1)


N = int(input())

tsp = TSP(N)
tsp.search(0, 1)

for city in tsp.order:
	print(city)


