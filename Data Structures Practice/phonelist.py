

def maketree(word, tree):
	node = tree
	index = 0
	for c in word:
		if c in node:
			node = node[c]
		else:
			node[c] = {}
			node = node[c]
		index += 1


def find(word, tree):
	node = tree
	success = True
	index = 0
	for c in word:
		if c in node:
			node = node[c]
			if (index == len(word) - 1) and len(node) > 0:
				success = False
				break
		else:
			break
		index += 1
	return success


t = int(input())

for _ in range(t):
	tree = {}
	n = int(input())
	result = True
	numbers = []
	for _ in range(n):
		number = input()
		numbers.append(number)
		maketree(number, tree)

	for i in range(n):
		if not find(numbers[i], tree):
			result = False

	print("YES" if result else "NO")
