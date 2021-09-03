from heapq import heappop, heappush


class Kruskal:
  def __init__(self, n):
    self.unionFind = {}
    for i in range(n):
      self.unionFind[i] = i
    self.edges = []

  def add_edges(self, m):
    for _ in range(m):
      u, v, f = map(int, input().split())
      if u < v:
        heappush(self.edges, (f, u, v))
      elif v < u:
        heappush(self.edges, (f, v, u))

  # this finds the root and also redirects all nodes on the way to the root
  def find_root(self, name):
    if not self.unionFind[name] == name:
      self.unionFind[name] = self.find_root(self.unionFind[name])
    return self.unionFind[name]

  def mst(self):
    accepted = []
    score = 0

    i = 0
    while len(self.edges) > 0:
      weight, x, y = heappop(self.edges)
      root1 = self.find_root(x)
      root2 = self.find_root(y)
      # print("loop " + str(i) + ": (f, x, y): (" + str(weight) + ", " + str(x) + ", " + str(y) + ")")
      i += 1
      # print(self.unionFind)
      if not root1 == root2:
        # print("success")
        self.unionFind[root1] = root2
        heappush(accepted, (x, y))
        score += weight

    return accepted, score

n, m = map(int, input().split())

while not n == 0:
  k = Kruskal(n)
  k.add_edges(m)
  result, score = k.mst()
  if len(result) < n - 1:
    print('Impossible')
  else:
    print(score)
    result = sorted(result, key=lambda z: (z[1]))
    result = sorted(result, key=lambda z: (z[0]))
    # ordered1 = sorted(result, key=lambda k: (k[1]))
    # ordered = sorted(ordered1, key=lambda k: (k[0]))
    for _ in result:
      print(*edge)

  n, m = map(int, input().split())