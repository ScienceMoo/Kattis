n = int(input())

languages = list(map(int, input().split(" ")))

previous = {}

min_dif = n

for i,x in enumerate(languages):
    if x in previous:
        diff = i - previous[x]
        previous[x] = i

        if diff < min_dif:
            min_dif = diff
    else:
        previous[x] = i

print(min_dif)