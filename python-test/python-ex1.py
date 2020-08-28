# Find numbers which are divisible by 7 and 5 between 1500 and 2700 (both included)
l = []

for value in range(1500, 2701):
	if value%7==0 and value%5==0:
		l.append(value)

print(l)	