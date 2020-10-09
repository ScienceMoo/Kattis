import math
import sys


class Coord:
	def __init__(self, pX, pY):
		self.x = pX
		self.y = pY


def get_distance(coord_1, coord_2):
	a = int(coord_1.x - coord_2.x)
	b = int(coord_1.y - coord_2.y)
	return math.sqrt((a ** 2) + (b ** 2))


def crane_success(crane_coord, pLength, pWidth, maximum):
	result = [False, False, False, False]

	walls = [Coord(- (pLength / 2), 0), \
					 Coord((pLength / 2), 0), \
					 Coord(0, - (pWidth / 2)), \
					 Coord(0, (pWidth / 2))]

	for i in range(4):
		if get_distance(crane_coord, walls[i]) < maximum:
			result[i] = True

	return result


# recursive search for groups of cranes that are sufficient
def search_for_lowest_num(walls_reached_so_far, cranes_used_so_far, lowest_num_so_far, remaining_spots):
	# print("Searching for arrangements!")
	# print("cranes_used_so_far: " + str(cranes_used_so_far))
	# print(walls_reached_so_far)
	# print(remaining_spots)

	lowest_num = lowest_num_so_far

	if cranes_used_so_far >= lowest_num_so_far:
		# print("too many cranes")
		return lowest_num_so_far
	else:
		for index in range(len(remaining_spots)):
			new_result = []

			# print(remaining_spots[index])
			for k in range(4):
				new_result.append(remaining_spots[index][k] or walls_reached_so_far[k])

			# print(new_result)
			if False not in new_result and (cranes_used_so_far + 1 <= lowest_num):
				# print("SUCCESS")
				lowest_num = cranes_used_so_far + 1
			else:
				if index < (len(remaining_spots) - 1):
					# print("keep searching")
					# cut the array at the index so that all the arrangements are distinct
					spots_still_left = remaining_spots[(index + 1):]
					next_result = search_for_lowest_num(new_result, cranes_used_so_far + 1, lowest_num, spots_still_left)
					if next_result < lowest_num:
						lowest_num = next_result
				# else:
					# print("stop searching")

	if lowest_num < lowest_num_so_far:
		return lowest_num
	else:
		return lowest_num_so_far


def get_least_number(crane_options, pLength, pWidth, maximum):

	crane_successes = []
	# first check if it can be done with only 1 crane
	for one_crane in crane_options:
		success = crane_success(one_crane, pLength, pWidth, maximum)
		if False not in success:
			return 1
		crane_successes.append(success)


# get lines and remove newline character
lines = list(map(str.rstrip, sys.stdin))

info = lines[0].split(" ")

length = int(info[0])
width = int(info[1])
n = int(info[2])
r = int(info[3])

options = []

for line in lines[1:]:
	xCoord = int(line.split(" ")[0])
	yCoord = int(line.split(" ")[1])
	options.append(Coord(xCoord, yCoord))

walls_reached = [False, False, False, False]

cranes = []

for o in options:
	cranes.append(crane_success(o, length, width, r))

answer = search_for_lowest_num(walls_reached, 0, 5, cranes)
if answer != 5:
	print(answer)
else:
	print("Impossible")



