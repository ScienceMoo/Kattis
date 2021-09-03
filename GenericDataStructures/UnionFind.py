

# Union-Find Structure
class UnionFind:

	def __init__(self):
		self.NODES = {}

	# Node contains the root and also the size of the network
	class Node:
		def __init__(self, root):
			self.ROOT = root
			self.SIZE = 1

		def increment_size(self):
			self.SIZE += 1

	# return (True, size) if they're already in the same group
	# return (False, new_size) if merged two groups
	def add(self, name, other):
		# if the first one is not in the network yet
		if name not in self.NODES:
			self.NODES[name] = self.Node(name)

		# if the second one is not in the network
		if other not in self.NODES:
			root = self.find_root(name)
			# add 1 to the root's size
			self.NODES[root].increment_size()
			self.NODES[other] = self.Node(root)
		else:
			root1 = self.find_root(name)
			root2 = self.find_root(other)

			if root1 == root2:
				if not self.NODES[root1].SIZE == self.NODES[root2].SIZE:
					raise Exception("Problem with size system")
				return True, self.NODES[root1].SIZE
			# otherwise merge networks
			new_size = self.NODES[root1].SIZE + self.NODES[root2].SIZE
			self.NODES[root1].SIZE = new_size
			self.NODES[root2].SIZE = new_size
			self.NODES[root1].ROOT = root2
			return True, new_size

	# this finds the root and also redirects all nodes on the way to the root
	def find_root(self, name):
		if not self.NODES[name].ROOT == name:
			self.NODES[name].ROOT = self.find_root(self.NODES[name].ROOT)
		return self.NODES[name].ROOT

	def contains(self, name):
		return self.NODES.get(name) is not None

	def get(self, name):
		return self.NODES[name]

	def get_size(self, name):
		return self.find_root(name).SIZE

	def num_groups(self):
		unique = []
		for x in self.NODES:
			root = self.find_root(x)
			if root not in unique:
				unique.append(root)
		return len(unique)


