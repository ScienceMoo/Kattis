num_bites = int(input())

words = input().split()

current = 0
fishy = False

for word in words:
	current += 1
	if word == "mumble":
		continue
	if not int(word) == current:
		fishy = True

print("makes sense" if not fishy else "something is fishy")