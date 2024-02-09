# 45 dnd stats by Ashley Betchart
# Co-authors: Ashley, Aman

import random 

games = 1000000
total = 0
for i in range(games):
	a = 0
	for j in range(3):
		a += random.randint(1,6)
	total += a 
print(total/games)
