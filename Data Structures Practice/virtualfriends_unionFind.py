import sys


# Node contains the root and also the size of the network
class Node:
	def __init__(self, root):
		self.ROOT = root
		self.SIZE = 1

	def increment_size(self):
		self.SIZE += 1


# Union-Find Structure
class Network:

	def __init__(self):
		self.NODES = {}

	# new person that isnt in the network yet
	def add(self, name, root):
		self.NODES[name] = Node(root)

	# this finds the root and also redirects all nodes on the way to the root
	def find_root(self, name):
		if self.NODES[name].ROOT == name:
			return name
		else:
			new_root = self.find_root(self.NODES[name].ROOT)
			self.NODES[name].ROOT = new_root
			return new_root
		
	def contains(self, name):
		return self.NODES.get(name) is not None

	def get(self, name):
		return self.NODES[name]

	def get_size(self, name):
		return self.NODES[name].SIZE

	# this merges two social networks and adds the size, if they not already in the same network
	def redirect_root(self, name, root):
		previous = self.find_root(name)
		size = self.NODES[previous].SIZE + self.NODES[root].SIZE
		if not self.NODES[previous].ROOT == root:
			self.NODES[previous].SIZE = size
			self.NODES[root].SIZE = size
			self.NODES[previous].ROOT = root


# get lines and remove newline character
lines = list(map(str.rstrip, sys.stdin))

index = 1

while index < len(lines):
	line = lines[index]

	# initialize the Network
	numF = int(line)

	network = Network()

	for i in range(numF):
		index += 1
		friendship = lines[index]
		friends = friendship.split(" ")

		# if the first friend is not in the network yet
		if not network.contains(friends[0]):
			network.add(friends[0], friends[0])

		# if the second friend is not in the network
		if not network.contains(friends[1]):
			root = network.find_root(friends[0])
			network.add(friends[1], root)
			# add 1 to the root's size
			network.get(root).increment_size()
			# print result
			print(network.get_size(root))
		else:
			root = network.find_root(friends[1])
			# merge networks
			network.redirect_root(friends[0], root)
			# print result
			print(network.get_size(root))

	index += 1
