import math
import random

nts = 'ACGT'
for nt in nts:
		print(nt, 'end')
print()

import random

for i in range(20):
	print(random.choice(nts), end ='')


for i in range(3):
	print(".seq-", sep = '')
	for j in range(random.randint(20, 50)):
		print(random.choice(nts), end='')
		print()

for nt1 in nts:
	for nt2 in nts:
		print('outer', nt1, 'inner', nt2)

# print the matrix
limit = len(nts)
for i in range(0, limit):
	for j in range(0, limit):
		if i == j: print('+', end= ' ')
		else: print('-', end = ' ')