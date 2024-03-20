# 62 skewer by Ashley Betchart
# Co-authors: Ashley, Aman

import mcb185
import sys

w = 1000
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	g = seq[:w].count('G')
	c = seq[:w].count('C')
	for i in range(1, len(seq) -w +1):
		left = seq[i-1]
		right = seq[1+w-1]

		if left == 'G': g -= 1
		elif left == 'C': c -= 1

		if right == 'G': g += 1
		elif right == 'C': c +=1

		gc_comp = (c + g) / w
		if (c + g) > 0: gc_skew = (g - c) / (g + c)
		else: gc_skew = 0
		print(i, gc_comp, gc_skew)

#python3 62skewer.py ../MCB185/data/GCF_000005845.2_ASM584v2_protein.faa.gz
