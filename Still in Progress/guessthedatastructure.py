import sys
from queue import PriorityQueue

# get lines and remove newline character
lines = list(map(str.rstrip, sys.stdin))

index = 0

while index < len(lines):
    line = lines[index]

    queue = []
    isQueue = True
    stack = []
    isStack = True
    pq = PriorityQueue()
    isPQ = True

    for i in range(int(line)):
        index = index + 1
        nextLine = lines[index]
        values = nextLine.split(" ")

        if int(values[0]) == 1:
            queue.append(int(values[1]))
            stack.append(int(values[1]))
            pq.put(int(values[1]))
        else:
            if len(queue) == 0:
                isQueue = False
            elif int(values[1]) != queue.pop(0):
                isQueue = False

            if len(stack) == 0:
                isStack = False
            elif int(values[1]) != stack.pop():
                isStack = False

            if pq.qsize() == 0:
                isPQ = False
            elif int(values[1]) != pq.get():
                isPQ = False

    if isQueue:
        if isStack:
            print("not sure")
        elif isPQ:
            print("not sure")
        else:
            print("queue")
    elif isStack:
        if isPQ:
            print("not sure")
        else:
            print("stack")
    elif isPQ:
        print("priority queue")
    else:
        print("impossible")


    index = index + 1
