# 73 missing kmers by Ashley Betchart
# Co-authors: Ashley, Aman

import sys
import mcb185
import itertools

for k in range(1, 10):
	kcount = {}
	for defline, seq in mcb185.read_fasta(sys.argv[1]):
		rev = mcb185.anti_seq(seq)
		for i in range(len(seq) -k +1):
			kmer = seq[i:i+k]
			revk = rev[i:i+k]
			if kmer not in kcount: kcount[kmer] = 0
			if revk not in kcount: kcount[revk] = 0
			kcount[kmer] += 1
			kcount[revk] += 1
	if len(kcount.keys()) == 4**k: continue
	for ktup in itertools.product('ACGT', repeat=k):
		kmer = ''.join(ktup)
		if kmer not in kcount: print(kmer)
# python3 73missingkmers.py ../MCB185/data/GCF_000005845.2_ASM584v2_genomic.fna.gz



#look at again, need to get 52