# 57 birthday by Ashley Betchart
#Co-authors: Ashley, Aman

import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

total = 0
for i in range(trials):
	calendar = []
	for j in range(days):
		calendar.append(0)
	for k in range(people):
		birthday = random.randint(0, days - 1)
		calendar[birthday] += 1
	match = False
	for l in calendar:
		if l > 1:
			match = True
			break
	if match == True: total += 1
print(total/trials)