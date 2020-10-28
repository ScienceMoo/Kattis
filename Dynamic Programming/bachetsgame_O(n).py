import sys

# get lines and remove newline character
lines = list(map(str.rstrip, sys.stdin))

for line in lines:
	game = line.split()
	num_stones = int(game[0])
	nums = int(game[1])

	moves = list(map(int, game[2:]))

	# initialize array assuming that ollie always wins
	pos = [0] * (num_stones + 1)

	moves.sort()

	# 0 is ollie wins, 1 is stan wins
	pos[0] = 0

	# calculate win or loss at all positions
	for i in range(num_stones):
		if pos[i] == 0:
			# for i where adding max moves is less than total stones
			if i < num_stones - moves[nums-1]:
				# loop through all moves
				for j in range(nums):
					# i is a losing state (pos[i]=0), so if you can get there with a move you force the other player to lose
					pos[i+moves[j]] = 1
			else:
				# loop through all moves
				for j in range(nums):
					# if can force a loss under max stones, then you win
					if i + moves[j] <= num_stones:
						pos[i+moves[j]] = 1

	# Output results
	print("Stan wins" if pos[num_stones] == 1 else "Ollie wins")





