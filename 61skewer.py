# 61 skewer by Ashley Betchart
# Co-authors: Ashley, Aman

import dogma

seq = 'ACGTACGTGGGGGACGTACGTCCCCC'
w = 10
for i in range(len(seq) -w +1):
	s = seq[i:i+w]
	print(i, dogma.gc_comp(s), dogma.gc_skew(s))