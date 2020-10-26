import sys

# get lines and remove newline character
lines = list(map(str.rstrip, sys.stdin))

trees = list(map(int, lines[1].split()))

trees.sort(reverse=True)

# if there's no trees, then we can have the party on day 2
max_days = 1
count = 1

for tree in trees:
	# add 1 day to plant the tree
	count += 1
	if tree >= max_days:
		max_days = tree
	else:
		max_days -= 1

print(count + max_days)
