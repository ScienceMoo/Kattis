import sys
import math


class Ballot:

	def __init__(self, cities_array, num_c, num_b):
		self.cities = cities_array
		self.num_city = num_c
		self.num_box = num_b

	def binary_search(self, maximum_num_people, largest, smallest):
		# print("Binary Search")
		# print("M: " + str(maximum_num_people))
		distribution = []

		for city in self.cities:
			distribution.append(ballots_needed(maximum_num_people, city))

		if maximum_num_people == 1:
			return 1
		elif sum(distribution) > self.num_box:
			# print("Trying larger M")
			dif = (largest - maximum_num_people) / 2
			new_M = maximum_num_people + math.ceil(dif)
			return self.binary_search(new_M, largest, maximum_num_people)

		elif sum(distribution) < self.num_box:
			# print("Trying smaller M")
			dif = (maximum_num_people - smallest) / 2
			new_M = smallest + math.floor(dif)
			return self.binary_search(new_M, maximum_num_people, smallest)

		else:
			# print("found solution!!!")
			max_people = 0

			for k in range(len(self.cities)):
				if distribution[k] > 0:
					num_people = math.ceil(self.cities[k]/distribution[k])
					if num_people > max_people:
						max_people = num_people

			return max_people


def ballots_needed(max, pop):
	if max > 0:
		result = pop / max
		return math.ceil(result)
	else:
		return 0


# get lines and remove newline character
lines = list(map(str.rstrip, sys.stdin))

index = 0

while index < len(lines):
	line = lines[index]

	# initialize the Network
	num_cities = int(line.split(" ")[0])
	num_boxes = int(line.split(" ")[1])

	if not (num_cities <= 0 or num_boxes <= 0):
		the_cities = []
		total = 0
		largest_population = 0

		for i in range(num_cities):
			index += 1

			population = int(lines[index])
			if population > largest_population:
				largest_population = population
			total += population
			the_cities.append(population)

		ballot = Ballot(the_cities, num_cities, num_boxes)
		M = largest_population

		answer = ballot.binary_search(M, largest_population, 0)

		print(answer)

	index += 2

