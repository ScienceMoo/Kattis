import sys


def find_moves(the_board):
	n = len(the_board)

	moves = []

	for num in range(2 * n):
		moves.append([-1])

	moves_index = 0

	i = 0
	while i < (n-2):
		# check if a move is possible
		if (the_board[i] == True) and (the_board[i + 1] == True) and (the_board[i + 2] == False):
			moves[moves_index][0] = i
			moves[moves_index].append(i + 2)
			moves_index += 1
		i += 1

	y = n - 1
	while y >= 2:
		# check if a move is possible
		if (the_board[y] == True) and (the_board[y - 1] == True) and (the_board[y - 2] == False):
			moves[moves_index][0] = y
			moves[moves_index].append(y - 2)
			moves_index += 1
		y -= 1

	return moves


# execute a move and return a new board
def edit_board(start, end, current_board):
	new_board = []
	for i in range(len(current_board)):
		new_board.append(current_board[i])

	if start < end:
		new_board[start] = False
		new_board[start + 1] = False
		new_board[end] = True
	else:
		new_board[start] = False
		new_board[start - 1] = False
		new_board[end] = True

	return new_board


def execute(board):
	n = len(board)
	moves = find_moves(board)

	new_board = []
	for i in range(n):
		new_board.append(board[i])

	while moves[0][0] != -1:
		lowest_result = 12
		best_move = 0
		m = 0

		while moves[m][0] != -1 and m < 12:
			new_board2 = edit_board(moves[m][0], moves[m][1], new_board)
			result = execute(new_board2)
			if result < lowest_result:
				lowest_result = result
				best_move = m
			m += 1

		new_board3 = edit_board(moves[best_move][0], moves[best_move][1], new_board)
		for k in range(n):
			new_board[k] = new_board3[k]

		moves = find_moves(new_board)

	# count the pebbles
	pebbles_left = 0
	for x in range(n):
		if new_board[x]:
			pebbles_left += 1

	return pebbles_left


# get lines and remove newline character
lines = list(map(str.rstrip, sys.stdin))

# initialize the first digit using numbers 1-9
for line in lines[1:]:
	board = []
	min_left = 12

	# read the board
	for x in line:
		if x == '-':
			board.append(False)
		elif x == 'o':
			board.append(True)

	print(execute(board))
