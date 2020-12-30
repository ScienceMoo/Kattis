n = int(input())

while not n == -1:
	total = 0
	time_elapsed = 0
	for _ in range(n):
		s,t = map(int, input().split())
		t = (t - time_elapsed)
		total += s * t
		time_elapsed += t

	print(total, "miles")
	n = int(input())