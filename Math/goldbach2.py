

def is_prime(n):
	# removed these to save computation time
	# if n == 2 or n == 3: return True
	# if n < 2 or n%2 == 0: return False
	if n % 2 == 0: return False
	if n < 9: return True
	if n % 3 == 0: return False
	r = int(n**0.5)
	# since all primes > 3 are of the form 6n ± 1
	# start with f=5 (which is prime)
	# and test f, f+2 for being prime
	# then loop by 6.
	f = 5
	while f <= r:
		# print('\t',f)
		if n % f == 0: return False
		if n % (f+2) == 0: return False
		f += 6
	return True


num_tests = int(input())
prime_numbers = {2: True, 3: True, 4: False, 5: True}

for k in range(num_tests):
	number = int(input())
	L = int(number/2)

	results = []

	for i in range(2, L + 1):
		other = number - i
		if i not in prime_numbers:
			# print("adding first to dictionary")
			prime_numbers[i] = is_prime(i)
		if other not in prime_numbers:
			# print("adding other to dictionary")
			prime_numbers[other] = is_prime(other)
		if prime_numbers[i] and prime_numbers[other]:
			results.append((i, other))
		# print(i, prime_numbers[i])

	print(number, "has", len(results), "representation(s)")
	for i in range(len(results)):
		print(str(results[i][0]) + "+" + str(results[i][1]))
	print("")