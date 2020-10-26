import sys
import math

# get lines and remove newline character
lines = list(map(str.rstrip, sys.stdin))

n = int(lines[0])
days = 0
printers = 1
statues = 0

# keep printing printers until you have enough to print all statues in 1 day
while statues < n:
	if (n-statues) > printers:
		days += 1
		printers += printers
	else:
		days +=1
		statues += printers

print(days)