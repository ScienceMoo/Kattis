import sys


# a simple merge sort algorithm
def merge_sort(busNumbers):
    # if the list is empty or has only 1 item, return it
    length = len(busNumbers)
    if length <= 1:
        return busNumbers

    # split the list in half
    left = busNumbers[:(length // 2)]
    right = busNumbers[length // 2:]

    # recursively sort each half
    left = merge_sort(left)
    right = merge_sort(right)

    # merge the halves after they are sorted
    return merge(left, right)


def merge(left, right):
    result = []

    # create new list by going through the left and right simultaneously
    while not (len(left) == 0 or len(right) == 0):
        if int(left[0]) < int(right[0]):
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    # only one of these while loops will be executed, if there's leftover elements
    while not len(left) == 0:
        result.append(left.pop(0))

    while not len(right) == 0:
        result.append(right.pop(0))

    return result


# get lines and remove newline character
lines = list(map(lambda line: line.rstrip(), sys.stdin))

if int(lines[0]) > 0:
    busNumbers = lines[1].split(" ")

    sortedNumbers = merge_sort(busNumbers)

    # finally, find the sequences
    sequencing = False
    result = ""
    # for each number, check for number after it to see if its in the sequence
    for index in range(0, (len(sortedNumbers) - 1)):
        if not sequencing:
            result += sortedNumbers[index]

            # notice a sequence -> print the dash
            if index < len(sortedNumbers) - 2:
                if ((int(sortedNumbers[index]) + 1) == int(sortedNumbers[index+1])) and ((int(sortedNumbers[index]) + 2) == int(sortedNumbers[index+2])):
                    result += "-"
                    sequencing = True

                # otherwise print a space
                else:
                    result += " "
                    # otherwise print a space
            else:
                result += " "
        else:
            # if the sequence is over, print the final number in the sequence
            if not (int(sortedNumbers[index]) + 1) == int(sortedNumbers[index+1]):
                result += sortedNumbers[index] + " "
                sequencing = False

    # add last number
    result += str(sortedNumbers[-1])

    print(result)
