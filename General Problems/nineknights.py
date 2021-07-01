open_positions = [[True for _ in range(5)] for _ in range(5)]
valid = True
count = 0

for i in range(5):
    for j, thing in enumerate(input()):
        if thing == 'k' and not open_positions[i][j]:
            count += 1
            valid = False
            break   
        elif thing == 'k':
            count += 1
            if (i+1) < 5:
                if (j-2) >= 0:
                    open_positions[i+1][j-2] = False
                if (j+2) < 5:
                    open_positions[i+1][j+2] = False
                if (i+2) < 5:
                    if (j-1) >= 0:
                        open_positions[i+2][j-1] = False
                    if (j+1) < 5:
                        open_positions[i+2][j+1] = False
    else:
        continue  
    break

print("valid" if valid and count == 9 else "invalid")