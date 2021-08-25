N, K = map(int, input().split())

k = 0
crossed = [ False ] * ( N + 1 )

for i in range(2, N+1):
    if not crossed[i]:
        k += 1
        crossed[i] = True
       
        mult = 2
        current = i

        while k != K and current + i < N + 1:
            current += i
            if not crossed[i*mult]:
                k += 1
                crossed[i*mult] = True
            mult += 1
        if k == K:
            print(current)
            break