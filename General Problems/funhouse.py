W, L = map(int, input().split())

house = 1

while W != 0 and L != 0:
    print("HOUSE", house)
    room = []

    current_x = 0
    current_y = 0

    for l in range(L):
        line = input()
        room.append(['a' for _ in range(W)])
        for w in range(W):
            room[l][w] = line[w]
            if line[w] == '*':
                current_x = l
                current_y = w
    
    current = '*'
    direction_x = 1
    direction_y = 1

    if current_x == L-1:
        direction_x = -1
        direction_y = 0
    if current_x == 0:
        direction_y = 0
    if current_y == 0:
        direction_x = 0
    if current_y == W-1:
        direction_x = 0
        direction_y = -1

    while current != 'x':
        current_x += direction_x
        current_y += direction_y
    
        current = room[current_x][current_y]
        if current == '/':
            temp = direction_x
            direction_x = - direction_y
            direction_y = - temp
        if current == '\\':
            temp = direction_x
            direction_x = direction_y
            direction_y = temp
        if current == 'x':
            room[current_x][current_y] = '&'

        # for l in range(L):
        #     line = ""
        #     for w in range(W):
        #         if l == current_x and w == current_y:
        #             line += 'o'
        #         else:
        #             line += room[l][w]
        #         line += " "
        #     print(line)
    
    for l in range(L):
        line = ""
        for w in range(W):
            if l == current_x and w == current_y:
                line += '&'
            else:
                line += room[l][w]
        print(line)
    
    W, L = map(int, input().split())
    house += 1