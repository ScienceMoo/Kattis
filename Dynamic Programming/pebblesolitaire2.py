from sys import stdin

visited = set()


def pebble_solitaire(board):
	global visited
	score = 23

	if tuple(board) in visited:
		return score

	# save all positions (memoization)
	visited.add(tuple(board))

	for i in range(23):
		# Left
		if i > 1 and board[i] and board[i - 1] and not board[i - 2]:
			board[i] = board[i - 1] = 0
			board[i - 2] = 1
			# get lowest score for this move
			score = min(score, pebble_solitaire(board))
			board[i] = board[i - 1] = 1
			board[i - 2] = 0

		# Right
		if i < 21 and board[i] and board[i + 1] and not board[i + 2]:
			board[i] = board[i + 1] = 0
			board[i + 2] = 1
			# get lowest score for this move
			score = min(score, pebble_solitaire(board))
			board[i] = board[i + 1] = 1
			board[i + 2] = 0

	# get number of remaining pebbles
	return min(score, board.count(1))


n = int(stdin.readline())

for _ in range(n):
	board = [1 if c == 'o' else 0 for c in stdin.readline().strip()]
	print(pebble_solitaire(board))
	visited = set()