import sys


def number(n):
    switcher={
        '**** ** ** ****': 0,
        '  *  *  *  *  *': 1,
        '***  *****  ***': 2,
        '***  ****  ****': 3,
        '* ** ****  *  *': 4,
        '****  ***  ****': 5,
        '****  **** ****': 6,
        '***  *  *  *  *': 7,
        '**** ***** ****': 8,
        '**** ****  ****': 9
    }
    return switcher.get(n, "Invalid num")


# get lines and remove newline character
lines = list(map(str.rstrip, sys.stdin))

# first split the lines in chunks of 3 stars/spaces
linesSplit = [[lines[x][i:i+3] for i in range(0, len(lines[0]), 4)] for x in range(0, 5)]

# get the number of digits
numDigits = len(linesSplit[0])

# combine the various pieces to get the numbers as arrays of 3 bit chunks
numbers = [[linesSplit[x][i] for x in range(0, 5)] for i in range(0, numDigits)]

for i in range(0, 5):
    chunk = numbers[numDigits - 1][i]
    if len(chunk) == 1:
        numbers[numDigits - 1][i] += "  "
    elif len(chunk) == 2:
        numbers[numDigits - 1][i] += " "

# combine the chunks into the full number strings
numbersFull = ["".join(numbers[x]) for x in range(0, numDigits)]

# map the strings to actual integers
integers = list(map(number, numbersFull))

count = 0
invalid = False

# convert to a full integer number by multiplying each integer by exponents of 10
for num in range(0, numDigits):
    if integers[num] == "Invalid num":
        invalid = True
        break;
    count += (10 ** (numDigits - 1 - num)) * integers[num]

print("BEER!!" if count % 6 == 0 and not invalid else "BOOM!!")
