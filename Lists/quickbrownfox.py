import sys

for line in list(map(str.rstrip, sys.stdin))[1:]:
    # for every character in range 97 to 123, check if it is in the line
    missing_letters = list(filter(lambda c : chr(c) not in line.lower(), range(97, 123)))

    # convert the missing letters to characters, and append them to the message
    message = "missing " + ''.join(map(chr, missing_letters))

    # print result
    print(message if missing_letters else "pangram")

