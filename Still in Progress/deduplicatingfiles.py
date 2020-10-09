import sys


def hash_function(file):
	first = '{0:08b}'.format(ord(file[0]))
	result = list(map(int, [c for c in first]))

	for char in file[1:]:
		binary = '{0:08b}'.format(ord(char))
		bits = list(map(int, [c for c in binary]))
		for i in range(8):
			if result[i] == 1:
				if bits[i] == 1:
					result[i] = 0
				else:
					result[i] = 1
			else:
				if bits[i] == 1:
					result[i] = 1
				else:
					result[i] = 0

	key = "".join(list(map(str, result)))
	return int(key, 2)


class Node:
	def __init__(self, filename):
		self.filename = filename
		self.NEXT = None

	def get_next(self):
		return self.NEXT

	def set_next(self, node):
		self.NEXT = node


class HashTable:
	def __init__(self):
		self.files = {}

	def check_file(self, filename):
		key = hash_function(filename)
		if self.files.get(key) is not None:
			return is_unique(self.files[key], filename, 1)
		else:
			self.files[key] = Node(filename)
			return [True, 0]


def add_to_end(node, name, num):
	if node.get_next() is not None:
		return add_to_end(node.get_next(), name, num + 1)
	else:
		return num


def is_unique(node, new_file, num_collision):
	if node.filename == new_file:
		if node.get_next() is not None:
			more = add_to_end(node.get_next(), new_file, num_collision)
			return [False, more]
		else:
			return [False, num_collision]
	elif node.get_next() is not None:
		return is_unique(node.get_next(), new_file, num_collision + 1)
	else:
		node.set_next(Node(new_file))
		return [True, num_collision]


# get lines and remove newline character
lines = list(map(str.rstrip, sys.stdin))

index = 0

while index < len(lines):
	line = lines[index]

	# initialize the Network
	numF = int(line)

	fileSystem = HashTable()
	numUnique = 0
	numCollis = 0

	for i in range(numF):
		index += 1

		nextLine = lines[index]
		bool, numCols = fileSystem.check_file(nextLine)
		numCollis += numCols
		if bool:
			numUnique += 1

	if numF > 0:
		print(str(numUnique) + " " + str(numCollis))

	index += 1
import sys


def hash_function(file):
	first = '{0:08b}'.format(ord(file[0]))
	result = list(map(int, [c for c in first]))

	for char in file[1:]:
		binary = '{0:08b}'.format(ord(char))
		bits = list(map(int, [c for c in binary]))
		for i in range(8):
			if result[i] == 1:
				if bits[i] == 1:
					result[i] = 0
				else:
					result[i] = 1
			else:
				if bits[i] == 1:
					result[i] = 1
				else:
					result[i] = 0

	key = "".join(list(map(str, result)))
	return int(key, 2)


class Node:
	def __init__(self, filename):
		self.filename = filename
		self.NEXT = None

	def get_next(self):
		return self.NEXT

	def set_next(self, node):
		self.NEXT = node


class HashTable:
	def __init__(self):
		self.files = {}

	def check_file(self, filename):
		key = hash_function(filename)
		if self.files.get(key) is not None:
			return is_unique(self.files[key], filename, 1)
		else:
			self.files[key] = Node(filename)
			return [True, 0]


def add_to_end(node, name, num):
	if node.get_next() is not None:
		return add_to_end(node.get_next(), name, num + 1)
	else:
		return num


def is_unique(node, new_file, num_collision):
	if node.filename == new_file:
		if node.get_next() is not None:
			more = add_to_end(node.get_next(), new_file, num_collision)
			return [False, more]
		else:
			return [False, num_collision]
	elif node.get_next() is not None:
		return is_unique(node.get_next(), new_file, num_collision + 1)
	else:
		node.set_next(Node(new_file))
		return [True, num_collision]


# get lines and remove newline character
lines = list(map(str.rstrip, sys.stdin))

index = 0

while index < len(lines):
	line = lines[index]

	# initialize the Network
	numF = int(line)

	fileSystem = HashTable()
	numUnique = 0
	numCollis = 0

	for i in range(numF):
		index += 1

		nextLine = lines[index]
		bool, numCols = fileSystem.check_file(nextLine)
		numCollis += numCols
		if bool:
			numUnique += 1

	if numF > 0:
		print(str(numUnique) + " " + str(numCollis))

	index += 1
