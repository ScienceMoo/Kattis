A, B, C = map(int, input().split())
I, J, K = map(int, input().split())

max_drinks = min((A / I), (B / J), (C / K))

result = ((A - (I * max_drinks)), (B - (J * max_drinks)), (C - (K * max_drinks)))

print("%.6f %.6f %.6f" % result)

