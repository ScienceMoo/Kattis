import sys


# which key should be pressed for that character (n)
def number(n):
    switcher = {
        'a': 2,
        'b': 2,
        'c': 2,
        'd': 3,
        'e': 3,
        'f': 3,
        'g': 4,
        'h': 4,
        'i': 4,
        'j': 5,
        'k': 5,
        'l': 5,
        'm': 6,
        'n': 6,
        'o': 6,
        'p': 7,
        'q': 7,
        'r': 7,
        's': 7,
        't': 8,
        'u': 8,
        'v': 8,
        'w': 9,
        'x': 9,
        'y': 9,
        'z': 9,
        ' ': 0,
    }
    return switcher.get(n, "Invalid num")


# how many times should the key be pressed
def repeat(n):
    switcher = {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 1,
        'e': 2,
        'f': 3,
        'g': 1,
        'h': 2,
        'i': 3,
        'j': 1,
        'k': 2,
        'l': 3,
        'm': 1,
        'n': 2,
        'o': 3,
        'p': 1,
        'q': 2,
        'r': 3,
        's': 4,
        't': 1,
        'u': 2,
        'v': 3,
        'w': 1,
        'x': 2,
        'y': 3,
        'z': 4,
        ' ': 1,
    }
    return switcher.get(n, "Invalid num")


# get lines and remove newline character
lines = list(sys.stdin)

count = 1
for line in lines[1:]:
    result = ""
    index = 0
    previous = -1
    for letter in line:
        num = number(letter)
        rep = repeat(letter)
        if not num == "Invalid num":
            # insert a space if the letter requires the same button as the previous
            if (index > 0) and (num == previous):
                result += ' '
            # print the character with the correct number of repeats
            for i in range(0, rep):
                result += str(num)
        previous = num
        index += 1
    print("Case #" + str(count) + ": " + result)
    count += 1

