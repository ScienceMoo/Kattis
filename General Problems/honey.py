# OEIS integer list: https://oeis.org/A002898
seq = [-1 , 0, 6, 12, 90, 360, 2040, 10080, 54810, 290640, 1588356, 8676360, 47977776, 266378112, 1488801600]

num_tests = int(input())

for _ in range(num_tests):
	n = int(input())

	print(seq[n])

