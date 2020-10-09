import sys

# get lines and remove newline character
lines = list(map(str.rstrip, sys.stdin))

inputFile = lines[1]
outputFile = lines[2]

# find out whether the bits should be flipped
flip = not int(lines[0]) % 2 == 0

# check if each bit is correct by comparing it to the output
failed = list(filter(lambda c : (flip and inputFile[c] == outputFile[c]) or (not flip and not inputFile[c] == outputFile[c]), range(0, len(inputFile))))

# print results
print("Deletion failed" if failed else "Deletion succeeded")


