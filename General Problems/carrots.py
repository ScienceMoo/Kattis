import sys

# get lines and remove newline character
lines = list(map(str.rstrip, sys.stdin))

print(lines[0].split()[1])