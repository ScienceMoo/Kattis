n, code, guess = input().split()
r = 0
s = 0

leftover_code = []
leftover_guess = ''

for i, c in enumerate(code):
    if guess[i] == c:
        r += 1
    else:
        leftover_code.append(code[i])
        leftover_guess += guess[i]

for c in leftover_guess:
    if c in leftover_code:
        s += 1
        leftover_code.remove(c)

print(r, s)