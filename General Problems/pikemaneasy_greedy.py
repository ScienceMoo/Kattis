import sys

# get lines and remove newline character
lines = list(map(str.rstrip, sys.stdin))

first_line = list(map(int, lines[0].split()))
num_problems = first_line[0]
contest_time = first_line[1]

second_line = list(map(int, lines[1].split()))
A = second_line[0]
B = second_line[1]
C = second_line[2]

first_problem = second_line[3]

problems = [0] * num_problems

problems[0] = first_problem
for x in range(1, num_problems):
	problems[x] = (((A * problems[x-1]) + B) % C) + 1

problems.sort()

penalty = 0
problems_solved = 0
time = 0

while time < contest_time and len(problems) > 0:
	time_remaining = contest_time - time
	if problems[0] <= time_remaining:
		penalty += time + problems[0]
		time += problems[0]
		problems_solved += 1
	problems.pop(0)

penalty = int(penalty % 1000000007)
print(str(problems_solved) + " " + str(penalty))
