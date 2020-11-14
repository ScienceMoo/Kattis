tree = {}

def count(word):
	node = tree
	success = True
	for c in word:
		if c in node:
			node = node[c]
			node["count"] += 1
		else:
			node[c] = {"count" : 1}
			node = node[c]
			success = False
	if success:
		return node["count"] - 1
	return 0


N = int(input())

word_list = [input() for _ in range(N)]

for w in word_list:
	print(count(w))