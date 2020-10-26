import sys
import math

# get lines and remove newline character
lines = list(map(str.rstrip, sys.stdin))

diagonals_left = []
diagonals_right = []

rows = [[1 if c == '*' else 0 for c in line] for line in lines]
cols = [[1 if line[i] == '*' else 0 for line in lines] for i in range(len(rows[0]))]

valid = True
total = 0

for row in rows:
	total += row.count(1)
	if row.count(1) > 1:
		valid = False

for cols in cols:
	total += cols.count(1)
	if cols.count(1) > 1:
		valid = False

for index in range(8):
	diagonal = []
	for j in range(8 - index):
		diagonal.append(rows[j][index + j])
	total += diagonal.count(1)
	if diagonal.count(1) > 1:
		valid = False

for index in range(1, 8):
	diagonal = []
	for j in range(8 - index):
		diagonal.append(rows[index + j][j])
	total += diagonal.count(1)
	if diagonal.count(1) > 1:
		valid = False

for index in range(8):
	diagonal = []
	for j in range(index + 1):
		diagonal.append(rows[index - j][j])
	total += diagonal.count(1)
	if diagonal.count(1) > 1:
		valid = False

for index in range(1, 8):
	diagonal = []
	for j in range(0, 8 - index):
		diagonal.append(rows[7 - j][index + j])
	total += diagonal.count(1)
	if diagonal.count(1) > 1:
		valid = False

print("valid" if valid and (total == 32) else "invalid")