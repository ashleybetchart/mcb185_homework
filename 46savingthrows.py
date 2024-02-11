# 46 saving throws by Ashley Betchart
# Co-authors: Ashley, Aman

import random

def normal():
	return random.randint(1, 20)

def advantage():
	d1 = random.randint(1, 20)
	d2 = random.randint(1, 20)
	if d1 >= d2: return d1
	else: return d2

def disadvantage():
	d1 = random.randint(1, 20)
	d2 = random.randint(1, 20)
	if d1 <= d2: return d1
	else: return d2

games = 1000
for i in range(5, 16, 5):
	print(i, end = '\t')
	success = 0
	for j in range(games):
		a = advantage()
		if a >= i: success += 1
	print(success/games)

for i in range(5, 16, 5):
	print(i, end = '\t')
	success = 0
	for j in range(games):
		n = normal()
		if n >= i: success += 1
	print(success/games)

for i in range(5, 16, 5):
	print(i, end = '\t')
	success = 0
	for j in range(games):
		d = disadvantage()
		if d >= i: success += 1
	print(success/games)