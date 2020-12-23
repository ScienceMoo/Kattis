H, T = map(int, input().split())

dict = {}
visited = {}

for i in range(103):
	for j in range(103):
		dict[(i,j)] = float('inf')
		visited[(i, j)] = False

dict[(0, 0)] = 0
visited[(0, 0)] = True

queue = [(0,0)]

while not len(queue) == 0:
	a, b = queue.pop(0)
	val = dict[(a,b)]

	if b > 0:
		# cut off tail, 2 tails grow
		dict[(a, b-1)] = min(val + 1, dict[(a, b-1)])
		if not visited[(a, b-1)]:
			queue.append((a, b-1))
			visited[(a, b-1)] = True

	if a > 0:
		# cut off 2 tails, new head
		dict[(a-1, b+2)] = min(val + 1, dict[(a-1, b+2)])
		if not visited[(a-1, b+2)] and b+2 < 101:
			queue.append((a-1, b+2))
			visited[(a-1, b+2)] = True

	# cut off 2 heads, nothing happens
	dict[(a+2, b)] = min(val + 1, dict[(a+2, b)])
	if not visited[(a+2, b)] and a+2 < 101:
		queue.append((a+2, b))
		visited[(a+2, b)] = True

while not H == 0:
	print(dict[(H,T)])

	H, T = map(int, input().split())