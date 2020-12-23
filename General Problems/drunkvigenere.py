message = input()
key = input()

index = 0
new_word = ''
for i, c in enumerate(key):
	shift = ord(c) - 65
	current = ord(message[i])
	if index % 2 == 0:
		current -= shift
		if current < 65:
			current += 26
	else:
		current += shift
		if current > 90:
			current -= 26

	index += 1
	new_word += chr(current)

print(new_word)
