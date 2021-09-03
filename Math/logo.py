import math

num_tests = int(input())

for _ in range(num_tests):
	pos = (0, 0)
	current_angle = 0
	num_moves = int(input())

	for _ in range(num_moves):
		move = input().split()
		direction = move[0]
		amount = int(move[1])

		if (direction == 'fd') or (direction == 'bk'):
			angle = current_angle
			y_factor = 1
			x_factor = 1
			if current_angle > 270:
				angle = 360-angle
				y_factor = -1
			elif current_angle > 180:
				angle = angle - 180
				y_factor = -1
				x_factor = -1
			elif current_angle > 90:
				angle = 180 - angle
				x_factor = -1

			x_dif = x_factor * amount * math.cos(math.radians(angle))
			y_dif = y_factor * amount * math.sin(math.radians(angle))

			if (direction == 'fd'):
				pos = (pos[0] + x_dif, pos[1] + y_dif)
			else:
				# backward
				pos = (pos[0] - x_dif, pos[1] - y_dif)

		elif direction == 'lt':
			# left
			current_angle += amount
		elif direction == 'rt':
			# right
			current_angle -= amount

	result = round(math.sqrt((abs(pos[0])**2) + (abs(pos[1])**2)))
	print(result)