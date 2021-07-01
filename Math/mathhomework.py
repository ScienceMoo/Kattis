legs = list(map(int, input().split(" ")))

total = legs[3]

b, d, c = legs[:3]

possible = False

for i in range(round(total / b) + 1):
    for j in range(round(total / d) + 1):
        for k in range(round(total / c) + 1):
            if (i*b) + (j*d) + (k*c) == total:
                possible = True
                print(i, j, k)

if not possible:
    print("impossible")