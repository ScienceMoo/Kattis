def is_win(smaller, bigger):
    if bigger % smaller == 0: return True
    if bigger >= smaller * 2: return True
    return not is_win(bigger % smaller, smaller)


n, m = [int(i) for i in input().split()]
print('win' if is_win(min(n, m), max(n, m)) else 'lose')