import sys
import itertools

# get lines and remove newline character
lines = list(map(lambda line: line.rstrip('\n'), sys.stdin))


# this re-arranges the letters in a single chunk
def chunkify(chunk):
    chunk_split = [chunk[i:i + 1] for i in range(0, n, 1)]
    new_chunk_array = list(map(lambda i: chunk_split[key[i] - 1], range(0, n)))
    return "".join(new_chunk_array)


for index in itertools.count(0, 2):
    n, *key = map(int, lines[index].split(' '))

    if n == 0:
        break

    line = lines[index + 1]

    # first split the line into chunks of n
    lineSplit = [line[i:i+n] for i in range(0, len(line), n)]

    # make sure the message is not empty
    if not len(lineSplit) == 0:
        # make sure the last chunk is not too short
        lastChunkLength = len(lineSplit[-1])
        if lastChunkLength < n:
            lineSplit[-1] += ' ' * (n - lastChunkLength)

        newChunks = map(chunkify, lineSplit)
        print("'" + "".join(newChunks) + "'")

    else:
        print("''")
