import sys
import mcb185


# stepping through FASTA Files
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	print(defline[:30], seq[:40], len(seq))

# Calc GC comp of nt seq in FASTA file
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	defwords = defline.split()
	name = defwords[0]
	gc = 0
	for nt in seq:
		if nt == 'C' or nt == 'G': gc += 1
	print(name, gc/len(seq))
#use this w A.thaliana, C. elegans, D. melanogaster.fa.gz

# if-elif-else stack (indiv nt count)
A = 0
C = 0
G = 0
T = 0
N = 0
for nt in seq:
	if nt == 'A': A += 1
	elif nt == 'C': C += 1
	elif nt == 'G': G += 1
	elif nt == 'T': T += 1
	else:
		N += 1
print( name, A/len(seq), C/len(seq), G/len(seq), T/len(seq), N/len(seq))

# list variation, still if/elif/else but counts instead of variables
nts = 'ACGTN'
counts = []
for i in range(len(nts)): counts.append(0)
for nt in seq:
	if nt == 'A': counts[0] += 1
	elif nt == 'C': counts[1] += 1
	elif nt == 'G': counts[2] += 1
	elif nt == 'T': counts[3] += 1
	else:
		counts[4] += 1
print(name, end='\t')
for n in counts: print(f'{n/len(seq):.4f}', end='\t')
print()

# indexing w str.find(), replc if/elif/else w str.find(). 
# * initializes all counts to 0
nts = 'ACGTN'
counts = [0] * len(nts)
for nt in seq:
	idx = nts.find(nt)
	counts[idx] += 1
print(name, end='\t')
for n in counts: print(f'{n/len(seq):.4f}', end='\t')
print()

# counting w str.count to count specific letters
nts = 'ACGTN'
print(name, end='\t')
for nt in nts:
	print(seq.count(nt) / len(seq), end='\t')
print()


# sliding window algorithm
w = 10
s = 1
for i in range(0, len(seq) -w+1, s):
	subseq = seq[i:i+w]
# L1 = window size (w)
# L2 = step size (each codon 3nt apart).
# L3 = argument version of range
# L4: subseq as slice using i (cuurent) and w






