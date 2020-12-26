N, B = input().split()

dom_dict = {'A': 11, 'K': 4, 'Q': 3, 'J': 20, 'T': 10, '9': 14, '8': 0, '7': 0}
reg_dict = {'A': 11, 'K': 4, 'Q': 3, 'J': 2, 'T': 10, '9': 0, '8': 0, '7': 0}

count = 0

for _ in range(int(N)):
	for _ in range(4):
		c, s = map(lambda x: x, input())
		if s == B:
			count += dom_dict[c]
		else:
			count += reg_dict[c]

print(count)