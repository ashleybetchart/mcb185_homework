# 34 scoring matrix by Ashley Betchart
# Co-authors Ashley, Aman

A = 'ACGT'
for nt in A:
	print(' ', nt, end =' ')
print (' ')
for A1 in A:
	print(A1, end = ' ')
	for A2 in A:
		if A1 == A2: print('+1', end = ' ')
		else:		 print('-1', end = ' ')
	print(' ')