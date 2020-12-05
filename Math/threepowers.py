


# convert the index to binary
# the 1s and 0s indicate whether that value of the set is included in the subset
def print_set(n):
	shifts = 0
	result = []
	while n > 0:
		if n & 1 == 1:
			result.append(3 ** shifts)
		n >>= 1
		shifts += 1
	return result

# n = int(input())
#
# while not n == 0:
# 	r = print_set(n - 1)
# 	print('{ ', end='')
# 	if len(r) > 0:
# 		print('{:d}'.format(r[0]), end='')
# 	for thing in r[1:]:
# 		print(', {:d}'.format(thing), end='')
# 	print(' }')
# 	n = int(input())


# testing
# for n in range(1, 50):
# 	print(bin(n-1))
# 	r = print_set(n - 1)
# 	print(str(n), '{ ', end='')
# 	current = 3
# 	maxpower = 0
#
# 	if len(r) > 0:
# 		maxpower = max(r)
# 		if 1 in r:
# 			print('1', end='')
# 		else:
# 			print('_', end='')
# 	else:
# 		print('_', end='')
#
# 	while current <= maxpower:
# 		if current in r:
# 			print(', {:d}'.format(current), end='')
# 		else:
# 			if current > 99:
# 				print(', ___', end='')
# 			elif current > 9:
# 				print(', __', end='')
# 			else:
# 				print(', _', end='')
# 		current = current * 3
# 	print(' }')
