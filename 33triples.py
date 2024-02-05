# 33 triples by Ashley Betchart
# Co-authors: Ashley, Aman

import math

limit = 100
for i in range(1, limit):
	for j in range(i + 1, limit):
		c = math.sqrt(i**2 + j**2)
		if c % 1 == 0:
			print(i, j, c)