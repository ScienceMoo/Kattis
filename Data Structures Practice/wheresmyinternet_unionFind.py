import sys


class UnionFindNetwork:
	def __init__(self, num_houses):
		# initialize all houses rooted to themselves
		self.ROOTS = [r for r in range(num_houses + 1)]

	def find_root(self, index):
		# if the root does not point to itself (its not top level)
		if self.ROOTS[self.ROOTS[index]] != self.ROOTS[index]:
			self.ROOTS[index] = self.find_root(self.ROOTS[index])
		return self.ROOTS[index]


# get lines and remove newline character
lines = list(map(str.rstrip, sys.stdin))

total = int(lines[0].split()[0])
town = UnionFindNetwork(total)
cables = [list(map(int, line.split())) for line in lines[1:]]

# set or redirect roots
for i in range(len(cables)):
	root1 = town.find_root(cables[i][0])
	root2 = town.find_root(cables[i][1])
	if root1 < root2:
		town.ROOTS[root2] = root1
	else:
		town.ROOTS[root1] = root2

# make sure all roots are toplevel
for x in range(1, total + 1):
	town.ROOTS[x] = town.find_root(x)

# print result
if town.ROOTS.count(1) == total:
	print("Connected")
else:
	for h in range(1, total + 1):
		if town.ROOTS[h] != 1:
			print(h)
