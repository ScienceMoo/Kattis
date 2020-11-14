import sys


class UnionFindNetwork:
	def __init__(self, num_friends):
		# initialize all houses rooted to themselves
		self.ROOTS = [r for r in range(num_friends)]
		self.SUMS = [int(line) for line in lines[1:n+1]]

	def find_root(self, index):
		# if the root does not point to itself (its not top level)
		if self.ROOTS[self.ROOTS[index]] != self.ROOTS[index]:
			self.ROOTS[index] = self.find_root(self.ROOTS[index])
		return self.ROOTS[index]


# get lines and remove newline character
lines = list(map(str.rstrip, sys.stdin))

n = int(lines[0].split()[0])
town = UnionFindNetwork(n)
friendships = [list(map(int, line.split())) for line in lines[n+1:]]

# set or redirect roots
for i in range(len(friendships)):
	root1 = town.find_root(friendships[i][0])
	root2 = town.find_root(friendships[i][1])
	if root1 < root2:
		town.ROOTS[root2] = root1
	else:
		town.ROOTS[root1] = root2

# make sure all roots are toplevel
for x in range(n):
	town.ROOTS[x] = town.find_root(x)

sums = [0 for _ in range(n)]

# print result
for h in range(n):
	for h2 in range(n):
		if town.ROOTS[h2] == h:
			sums[h] += town.SUMS[h2]

if max(sums) == 0 and min(sums) == 0:
	print("POSSIBLE")
else:
	print("IMPOSSIBLE")
