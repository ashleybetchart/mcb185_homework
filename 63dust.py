# 63 dust by Ashley Betchart
# Co-authors: Ashley, Aman

import sys
import mcb185
import math

w = int(sys.argv[2])
threshold = float(sys.argv[3])

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	print(defline)
	out = list(seq)
	for i in range(1, len(seq) -w + 1):
		s = seq[i:i+w]
		ent = 0
		a = s.count('A')
		c = s.count('C')
		g = s.count('G')
		t = s.count('T')
		if a > 0: ent += (a / w) * math.log2(a / w)
		if c > 0: ent += (c / w) * math.log2(c / w)
		if g > 0: ent += (g / w) * math.log2(g / w)
		if t > 0: ent += (t / w) * math.log2(t / w)
		ent *= 1
		if ent < threshold:
			for j in range(w): out[i+j] = 'N'
	print(''.join(out))

# python3 63dust.py ../MCB185/data/GCF_000005845.2_ASM584v2_protein.fna.gz 20 4

###### python3 63dust.py ../MCB185/data/GCF_000005845.2_ASM584v2_protein.faa.gz 20 4

#python3 63dust.py ../MCB185/data/GCF_000005845.2_ASM584v2_genomic.fna.gz 20 4
#make changes to this,smthg wrong

