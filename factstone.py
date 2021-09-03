import math

bits_per_year = {year: i + 2 for i,year in enumerate(range(1960,2170,10))}
answers = {}
answers[2] = 3
answers[3] = 5
answers[4] = 8
answers[5] = 12
answers[6] = 20
answers[7] = 34
answers[8] = 57
answers[9] = 98
answers[10] = 170
answers[11] = 300
answers[12] = 536
answers[13] = 966
answers[14] = 1754
answers[15] = 3210
answers[16] = 5910
answers[17] = 10944
answers[18] = 20366
answers[19] = 38064
answers[20] = 71421
answers[21] = 134480
answers[22] = 254016


y = int(input())

while not y == 0:
	y = math.floor(y / 10) * 10
	print(answers[bits_per_year[y]])

	y = int(input())