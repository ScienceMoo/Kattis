import math
first_line = input().split(" ")
second_line = list(map(int, input().split(" ")))

M = int(first_line[0])
N = int(first_line[1])
R = float(first_line[2])

a_x = second_line[0]
a_y = second_line[1]
b_x = second_line[2]
b_y = second_line[3]

min_distance = math.pi * R

road_block_length = (R / N)
# print("road_block_length:", road_block_length)

for canal in range((max(a_y, b_y)) + 1):

    road_distance = (abs(canal - a_y) * road_block_length) + (abs(b_y - canal) * road_block_length)
    
    # print("b_y - a_y:", abs(b_y - a_y))
    # print("road_distance:", road_distance)

    new_radius = road_block_length * canal
    # print("new_radius:", new_radius)
    angle = abs(b_x - a_x) * (180 / M)
    # print("angle:", angle)
    # print("angle fraction:", (angle / 180))
    canal_distance = math.pi * new_radius * (angle / 180)
    # print("canal_distance:", canal_distance)

    total = canal_distance + road_distance
    if total < min_distance:
        min_distance = total

if total == 0:
    print("0")
else:
    print('{0:.14f}'.format(min_distance))