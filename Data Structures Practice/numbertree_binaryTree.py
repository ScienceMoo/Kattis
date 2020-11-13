# get input
line = input().split()
h = int(line[0])

# initialize at top of the tree
node = (2**(h+1)) - 1
level = 0 # current level
rightPenalty = 0 # extra penalty from right turns

# if there's a path
if len(line) > 1:
	path = line[1]

	for step in path:
		if step == 'L':
			# left turn
			reduction = (2 ** level) + rightPenalty
			node -= reduction
			rightPenalty *= 2
		else:
			# right turn
			reduction = (2 ** level) + rightPenalty + 1
			node -= reduction
			rightPenalty *= 2
			rightPenalty += 1
		level += 1

print(node)

