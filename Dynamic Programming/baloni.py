import sys

# get lines and remove newline character
lines = list(map(str.rstrip, sys.stdin))

balloons = list(map(int, lines[1].split()))

counts = [0] * 1000001

for balloon in balloons:
	# if we dont already have an arrow at that height then add arrow at height - 1
	if counts[balloon] == 0:
		counts[balloon-1] += 1
	# if we have already have an arrow at that height then move arrow down by 1
	else:
		counts[balloon - 1] += 1
		counts[balloon] -= 1

# count how many arrows we needed
arrows = 0
for i in range(100000):
	arrows += counts[i]

print(arrows)
