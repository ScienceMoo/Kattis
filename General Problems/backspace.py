import sys

# get lines and remove newline character
lines = list(map(str.rstrip, sys.stdin))

# get the only line
line = lines[0]

# start with an empty array
result = []

for x in line:
	if x == '<':
		# apply backspace and do not add character
		result.pop()
	else:
		# add character
		result.append(x)

print("".join(result))