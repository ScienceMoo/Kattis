n1,n2 = map(int, input().split())
num_ants = n1 + n2

word1, word2, = input(), input()

row1 = []
directions = []
for c in word1:
	row1.insert(0, c)
	directions.append(1)

ants = row1 + [c for c in word2]
directions += [0 for _ in range(len(word2))]

# print("".join(ants))
# print(directions)

T = int(input())

while T > 0:
	i = 0
	while i < num_ants - 1:
		if directions[i] == 1 and directions[i+1] == 0:
			temp = ants[i]
			temp2 = directions[i]
			ants[i] = ants[i+1]
			directions[i] = directions[i+1]
			ants[i+1] = temp
			directions[i+1] = temp2
			i += 2
		else:
			i += 1
	# print("\nT", T)
	# print("".join(ants))
	# print(directions)
	T -= 1

# print("\nend")
print("".join(ants))
# print(directions)