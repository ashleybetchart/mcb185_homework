# 45 dnd stats by Ashley Betchart
# Co-authors: Ashley, Aman

import random

games = 70000
total = 0
for i in range(games):
	score = 0
	for j in range(3):
		score += random.randint(1,6)
	total += score
print(total/games)

total = 0
for i in range(games):
	score = 0
	for j in range(3):
		if random.randint(1,6) == 1: random.randint(1,6)
		score += random.randint(1,6)
	total +=score
print(total/games)

total = 0
for i in range(games):
	score = 0
	for j in range(3):
		d1 = random.randint(1,6)
		d2 = random.randint(1,6)
		if d1 >= d2: score += d1
		elif d2 >= d1: score += d2
	total += score
print(total/games)

total = 0
for i in range(games):
	score = 0
	d1 = random.randint(1,6)
	d2 = random.randint(1,6)
	d3 = random.randint(1,6)
	d4 = random.randint(1,6)
	if d1 <= d2 and d1 <= d3 and d1 <= d4: score += d2 + d3 + d4
	elif d2 <= d1 and d2 <= d3 and d2 <= d4: score += d1 + d3 + d4
	elif d3 <= d1 and d3 <= d2 and d3 <= d4: score += d1 + d2 + d4
	else: score = d1 + d2 + d3
	total += score
print(total/games)
