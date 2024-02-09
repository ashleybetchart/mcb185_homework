# 43 random dna by Ashley Betchart
# Co-authors: Ashley, Aman

import random

a = 3
nts = 'ACGT'									# number of sequences

for i in range(a):
	print(f'>seq-{i+1}')
	for j in range(random.randint(50, 60)):
		print(random.choice(nts), end = '')
	print()