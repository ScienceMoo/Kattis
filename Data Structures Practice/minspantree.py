from heapq import heappop, heappush


class Graph:
  def __init__(self, n, m):
    self.n = n
    self.edges = {}
    for i in range(n):
      self.edges[i] = []
    for _ in range(m):
      x, y, f = map(int, input().split())
      self.edges[x].append((f, y))
      self.edges[y].append((f, x))

  def mst(self):
    visited = [True] + [False] * (self.n - 1)
    edges = []
    totalScore = 0
    # we dont need to use best for it to work, it just speeds it up
    best = [float('inf')] * self.n
    remaining = set(range(self.n))
    remaining.remove(0)
    heap = []

    # initialize best for all is their edge with first one
    for e in self.edges[0]:
      weight = e[0]
      neighbour = e[1]
      # push (f, x, y)
      heappush(heap, (weight, 0, neighbour))
      best[neighbour] = weight

    # Search
    while len(heap) > 0:
      # pop from the heap and check that v has not been visited already
      score, previous, current = heappop(heap)
      if not visited[current] or (score < 0):
        # the smallest edge is the best one
        if previous < current:
          edges.append((previous, current))
        else:
          edges.append((current, previous))
        totalScore += score
        visited[current] = True
        remaining.remove(current)
        # for all not visited
        for f, nxt in self.edges[current]:
          if f < best[nxt] and (not visited[nxt]):
            best[nxt] = f
            heappush(heap, (f, current, nxt))

    if len(edges) < self.n - 1:
      return float('inf'), edges
    return totalScore, edges

n, m = map(int, input().split())

while not n == 0:
  g = Graph(n, m)
  mst_len, mst = g.mst()

  print("N: " + str(n))
  print("mst_len: " + str(mst_len))

  # output results
  print(mst_len if not mst_len == float('inf') else 'Impossible')

  if not mst_len == float('inf'):
    ordered = sorted(mst, key=lambda k: (k[0]))
    for edge in ordered:
      print(*edge)

  n, m = map(int, input().split())