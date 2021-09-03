# Shoelace Theorem
# https://artofproblemsolving.com/wiki/index.php/Shoelace_Theorem

n = int(input())

while not n == 0:
	points = []
	for _ in range(n):
		x,y = map(int, input().split())
		points.append((x,y))

	total = 0
	i = 0
	j = 1
	while i < n:
		total += points[i][0] * points[j][1]
		total -= points[i][1] * points[j][0]
		i += 1
		j = (j+1) % n

	total = total / 2
	if total < 0:
		print("CW %.1f" % - total)
	else:
		print("CCW %.1f" % total)

	n = int(input())