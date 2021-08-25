N, p = map(int, input().split())

cars = list(map(int, input().split()))
cars = sorted(cars)

first_car = cars[0]
min_distance = p
n = 0

for car in cars:
    dist = p * (n+1) - (car - first_car)
    if dist > min_distance:
        min_distance = dist
    n += 1

print(min_distance)