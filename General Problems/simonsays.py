n = int(input())

for _ in range(n):
	sentence = input()
	if "Simon says " in sentence:
		print(sentence.split("Simon says ")[1 ])