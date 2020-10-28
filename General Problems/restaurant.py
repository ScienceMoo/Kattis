import sys

# get lines and remove newline character
lines = list(map(str.rstrip, sys.stdin))

index = 0
while index < len(lines):
	number = int(lines[index])
	if index > 0 and number != 0:
		print("")
	index += 1

	pile1_height = 0
	pile2_height = 0

	for i in range(number):
		event = lines[index]
		index += 1

		if "DROP" in event:
			drop = int(event.split("DROP ")[1])
			print("DROP 2 " + str(drop))
			pile2_height += drop
		elif "TAKE" in event:
			take = int(event.split("TAKE ")[1])
			if pile1_height > 0:
				if pile1_height >= take:
					print("TAKE 1 " + str(take))
					pile1_height -= take
				else:
					print("TAKE 1 " + str(pile1_height))
					take -= pile1_height
					print("MOVE 2->1 " + str(pile2_height))
					pile1_height = pile2_height
					pile2_height = 0
					print("TAKE 1 " + str(take))
					pile1_height -= take
			else:
				print("MOVE 2->1 " + str(pile2_height))
				pile1_height = pile2_height
				pile2_height = 0
				print("TAKE 1 " + str(take))
				pile1_height -= take
