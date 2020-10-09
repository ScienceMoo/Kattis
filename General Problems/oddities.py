import sys

# get lines and remove newline character
lines = list(map(str.rstrip, sys.stdin))

# for each line, check whether it's even and print the result
for line in lines[1:]:
    print(line + (" is even" if int(line) % 2 == 0 else " is odd"))
