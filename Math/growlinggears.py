num_tests = int(input())

for _ in range(num_tests):
	num_gears = int(input())

	# print(num_gears)

	highest = 0
	best_gear = 0

	for i in range(num_gears):
		a, b, c = map(int, input().split())

		R_max = b / (2*a)
		highest_torque = (- a * (R_max ** 2)) + (b * R_max) + c

		if highest_torque > highest:
			highest = highest_torque
			best_gear = i + 1


	print(best_gear)