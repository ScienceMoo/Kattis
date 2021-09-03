import operator

N, t = map(int, input().split())

A = list(map(int, input().split()))

# find two integers that sum to 7777
if t == 1:
	success = False
	for x in range(N):
		for i in range(x):
			if not (A[x] == A[i]) and (A[x] + A[i] == 7777):
				success = True
				break
		if success:
			break
	print("Yes" if success else "No")

# find out if all the numbers are unique
elif t == 2:
	unique = []
	for x in range(N):
		if not x in unique:
			unique.append(x)
	print("Unique" if len(unique) == N else "Contains duplicate")

# find out if one integer is repeated more than N/2 times
elif t == 3:
	counts = {}
	threshold = N/2
	for x in range(N):
		if not A[x] in counts:
			counts[A[x]] = 1
		else:
			counts[A[x]] += 1

	result = max_key = max(counts, key=lambda k: counts[k])
	print(result if (counts[result] > N/2) else -1)

# print the median of A
elif t == 4:
	sorted = sorted(A)
	idx = round(len(sorted) / 2)
	if len(sorted) % 2 == 0:
		print(str(sorted[idx-1]) + " " + str(sorted[idx]))
	else:
		print(sorted[idx])

# print integers in the range [100-999]
else:
	result = []
	sorted = sorted(A)
	x = sorted.pop(0)
	while x < 100:
		x = sorted.pop(0)
	while x >= 100 and x <= 999:
		result.append(str(x))
		x = sorted.pop(0)
	print(" ".join(result))