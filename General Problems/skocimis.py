import math

A,B,C = map(int, input().split())

min_k = min(A,B,C)
max_k = max(A,B,C)

AB = abs(A - B)
BC = abs(B - C)
AC = abs(A - C)

biggest = max(AB, BC, AC)

if not (A == min_k or A == max_k):
	biggest = max(AB, AC)
elif not (B == min_k or B == max_k):
	biggest = max(AB, BC)
elif not (C == min_k or C == max_k):
	biggest = max(AC, BC)

moves = 0
while biggest > 1:
	moves += 1
	# print("move", moves)
	if AB == biggest:
		C = min(A, B) + 1
	elif BC == biggest:
		A = min(B, C) + 1
	elif AC == biggest:
		B = min(A, C) + 1

	min_k = min(A, B, C)
	max_k = max(A, B, C)

	AB = abs(A - B)
	BC = abs(B - C)
	AC = abs(A - C)

	if not (A == min_k or A == max_k):
		biggest = max(AB, AC)
	elif not (B == min_k or B == max_k):
		biggest = max(AB, BC)
	elif not (C == min_k or C == max_k):
		biggest = max(AC, BC)

print(moves)