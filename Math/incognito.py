test = int(input())

for _ in range(test):
    counts = {}
    n = int(input())

    for _ in range(n):
        category = input().split(" ")[1]
        if category in counts:
            counts[category] += 1
        else:
            counts[category] = 1    

    sum = 1
    if len(counts) == 1:
        for thing in counts:
            print(counts[thing])
    else:
        for thing in counts:
            sum *= (counts[thing] + 1)
    
        print(sum - 1)




