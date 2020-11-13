import sys

# get lines and remove newline character
lines = list(map(str.rstrip, sys.stdin))

first_line = list(map(int, lines[0].split()))

num_movies = first_line[0]
scores = [float('inf')] * num_movies

visited = [False] * num_movies

similarities = [[] for _ in range(num_movies)]
stack = list(map(int, lines[1].split()))

for s in stack:
	scores[s] = 0

for line in lines[2:]:
	movies = list(map(int, line.split()))
	similarities[movies[0]].append(movies[1])
	similarities[movies[1]].append(movies[0])

while len(stack) > 0:
	i = stack.pop(0)
	if not visited[i]:
		visited[i] = True
		for movie in similarities[i]:
			scores[movie] = min(scores[i] + 1, scores[movie])
			stack.append(movie)

# print(scores)
print(scores.index(max(scores)))