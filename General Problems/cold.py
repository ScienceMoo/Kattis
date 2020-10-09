import sys

# get the inputs
inputList = list(map(str.rstrip, sys.stdin))[1].split(" ")

# count the number of negative numbers
count = len(list(filter(lambda c : int(c) < 0, inputList)))

print(count)
