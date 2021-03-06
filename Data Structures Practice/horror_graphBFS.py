import sys


# get lines and remove newline character
lines = list(map(str.rstrip, sys.stdin))

first_line = list(map(int, lines[0].split()))

num_movies = first_line[0]
scores = [float('inf')] * num_movies

visited = [False] * num_movies

similarities = [[] for _ in range(num_movies)]
horror_list = list(map(int, lines[1].split()))

for line in lines[2:]:
	movies = list(map(int, line.split()))
	similarities[movies[0]].append(movies[1])
	similarities[movies[1]].append(movies[0])

stack = []

for h in horror_list:
	visited[h] = True
	scores[h] = 0
	for o in similarities[h]:
		stack.append((h, o))

while len(stack) > 0:
	i, j = stack.pop(0)
	if not visited[j]:
		scores[j] = scores[i] + 1
		visited[j] = True
		for movie in similarities[j]:
			stack.append((j, movie))

print(scores)
print(scores.index(max(scores)))