n = int(input())

comm = list(map(int, input().split()))
result = []

for number in comm:
	retrieved = []

	scrambled_byte = bin(number)[2:]

	for _ in range(8 - len(scrambled_byte)):
		scrambled_byte = "0" + scrambled_byte

	i = 7

	scrambled = scrambled_byte[i]
	i -= 1

	if int(scrambled) == 1:
		retrieved.append('1')
	else:
		retrieved.append('0')

	while i >= 0:
		scrambled = scrambled_byte[i]

		if (int(scrambled) == 1) and (retrieved[0] == '1'):
			retrieved.insert(0, '0')
		elif (int(scrambled) == 1) and (retrieved[0] == '0'):
			retrieved.insert(0, '1')
		elif (int(scrambled) == 0) and (retrieved[0] == '0'):
			retrieved.insert(0, '0')
		else:
			retrieved.insert(0, '1')
		i -= 1

	result.append(str(int("0b" + "".join(retrieved), 2)))

print(" ".join(result))