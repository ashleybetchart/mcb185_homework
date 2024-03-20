# profinder by Ashley Betchart
# Co-authors: Ashley, Aman

import mcb185
import sys
import dogma

def getpro(aa, size):
	subset = []
	for orf in aa.split('*'):
		if 'M' in orf:
			start = orf.find('M')
			protein = orf[start:]
			if len(protein) >= size:
				subset.append(protein)
	return subset

def process(seq, size):
	subset = []
	for i in range(3):
		aa = dogma.translate(seq[i:])
		for protein in getpro(aa, size):
			subset.append(protein)
	rev_aa = dogma.revcomp(seq)
	for i in range(3):
		aa = dogma.translate(rev_aa[i:])
		for protein in getpro(aa, size):
			subset.append(protein)
	return subset

size = int(sys.argv[2])
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	proteins = process(seq, size)
	for i, protein in enumerate(proteins):
		id = f'{defline.split()[0]}-prot-{i+1}'
		print(f'>{id}\n{protein}')

#python3 64profinder.py ../MCB185/data/GCF_000005845.2_ASM584v2_genomic.fna.gz 100