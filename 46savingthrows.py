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
	adv = 0
	dis = 0
	nor = 0
	for j in range(games):
		if advantage() >= i: adv += 1
		if normal() >= i: nor += 1
		if disadvantage() >= i: dis += 1
	print(adv/games, dis/games, nor/games)

