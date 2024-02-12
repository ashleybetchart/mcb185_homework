# 42 chicago by Ashley Betchart
# Co-authors: Ashley, Aman

import random
games = 100000 
totalscore = 0
zeroes = 0
for i in range(games):
	score = 0
	for target in range(2, 13):
		if random.randint(1,6) + random.randint(1,6) == target:
			score += target
	if score == 0: zeroes += 1
	totalscore += score
print(totalscore/games)
print(zeroes/games)