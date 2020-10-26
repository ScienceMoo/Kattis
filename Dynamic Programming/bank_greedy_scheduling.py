import sys

# get lines and remove newline character
lines = list(map(str.rstrip, sys.stdin))

time_until_close = int(lines[0].split()[1])

# abuse list comprehension to get all the people into an array
d = [list(map(int, line.split())) for line in lines[1:]]

# sort by amount of cash they have
ordered = sorted(d, reverse=True, key=lambda k: (k[0]))

schedule = [0] * (time_until_close)

for person in ordered:
	if schedule.count(0) == 0:
		# stop looking once we have filled the schedule
		break
	index = person[1]
	if index >= time_until_close:
		index = time_until_close - 1
	# if that spot in the schedule is already taken, try earlier
	while schedule[index] != 0 and index > 0:
		index -= 1
	# add the person if a spot is available
	if schedule[index] == 0:
		schedule[index] = person[0]

print(sum(schedule))
