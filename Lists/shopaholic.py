X = input()
prices = list(map(int, input().split(" ")))

prices.sort(reverse = True)

print(sum(prices[2::3]))