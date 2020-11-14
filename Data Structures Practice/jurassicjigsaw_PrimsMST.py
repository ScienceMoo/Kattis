from heapq import heappop, heappush


class Graph:
  def __init__(self, n):
    self.n = n
    self.edges = [[0] * n for _ in range(n)]

  def create_edges(self, n):
    sequences = [None] * n
    for i in range(n):
      sequences[i] = input()
      for j in range(i):
        self.edges[j][i] = unlikeliness(sequences[j], sequences[i])
        self.edges[i][j] = self.edges[j][i]

  def mst(self):
    # best starts as 0 for all of them
    best = [0] * self.n
    remaining = set(range(1, self.n))
    visited = [True] + ([False] * (self.n - 1))
    heap = []
    edges = []
    totalScore = 0
    for i in range(1, self.n):
      # use heap as priority queue to sort the edges
      heappush(heap, (self.edges[0][i], 0, i))
      # initialize best for all is their edge with first one
      best[i] = self.edges[0][i]

    # Search
    while len(edges) < self.n - 1:
      while True:
        # pop from the heap and check that v has not been visited already
        score, u, v = heappop(heap)
        if visited[v]:
          continue
        break
      # the smallest edge is the best one
      edges.append((u, v))
      totalScore += score
      visited[v] = True
      remaining.remove(v)
      # for all not visited
      for x in remaining:
        if self.edges[v][x] < best[x]:
          best[x] = self.edges[v][x]
          heappush(heap, (self.edges[v][x], v, x))
    return totalScore, edges


def unlikeliness(seq1, seq2):
  return sum(n1 != n2 for n1, n2 in zip(seq1, seq2))


num_sequences, _ = map(int, input().split())

g = Graph(num_sequences)
g.create_edges(num_sequences)
mst_len, mst = g.mst()

# output results
print(mst_len)
for edge in mst:
  print(*edge)