n, T = list(map(int, input().split()))

tasks = list(map(int, input().split()))

result = 0
index = 0
sum = tasks[0]
while sum <= T and index < len(tasks):
	result += 1
	index += 1
	if index < len(tasks):
		sum += tasks[index]

print(result)