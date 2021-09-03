
num_cards = int(input())

cards = list(map(int, input().split()))

stack = []

for card in cards:
	if (not len(stack) == 0) and ((stack[-1] + card) % 2 == 0):
		stack.pop()
	else:
		stack.append(card)

print(len(stack))