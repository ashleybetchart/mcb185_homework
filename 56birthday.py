# 56 birthday by Ashley Betchart
# Co-authors: Ashley, Aman

import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

total = 0
for i in range(trials):
	match = False
	birthdays = []
	for j in range(people):
		birthdays.append(random.randint(1, days))
	birthdays.sort()
	for j in range(people):
		if birthdays[j - 1] == birthdays[j]: match = True
	if match == True: total +=1
print(total/trials)