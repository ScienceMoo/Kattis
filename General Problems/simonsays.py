import sys

# get lines and remove newline character
lines = list(map(str.rstrip, sys.stdin))

# initialize the first digit using numbers 1-9
for line in lines[1:]:
	if "Simon says" in line:
		print(line.split("Simon says ")[1])