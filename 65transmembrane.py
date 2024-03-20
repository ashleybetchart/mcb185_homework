# 65 transmembrane by Ashley Betchart
# Co-authors: Ashley, Aman

import mcb185
import sys
import dogma

def kydoo_hydro(seqs):
	hydro = 0
	for aa in seqs:
		if aa == "A": hydro += 1.80
		elif aa == "C": hydro +=  2.50
		elif aa == "D": hydro +=  -3.50
		elif aa == "E": hydro +=  -3.50
		elif aa == "F": hydro +=  -2.80
		elif aa == "G": hydro +=  -0.40
		elif aa == "H": hydro +=  -3.20
		elif aa == "I": hydro +=  4.50
		elif aa == "K": hydro +=  -3.90
		elif aa == "L": hydro +=  3.8
		elif aa == "M": hydro +=  1.90
		elif aa == "N": hydro +=  -3.50
		elif aa == "P": hydro +=  -1.60
		elif aa == "Q": hydro +=  -3.50
		elif aa == "R": hydro +=  -4.5
		elif aa == "S": hydro +=  -0.80
		elif aa == "T": hydro +=  -0.70
		elif aa == "V": hydro +=  4.20
		elif aa == "W": hydro +=  -0.90
		elif aa == "Y": hydro +=  -1.30
	return hydro / len(seqs)

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	sigpep = False
	tmemb = False
	if len(seq) >30:
		for i in range(0, 23):
			if seq[1:1+8].find('P') == -1 and kydoo_hydro(seq[i:i+8]) >= 2.5: sigpep =  True
	if sigpep is True:
		for i in range(30, len(seq)-10):
			if seq[i:i+11].find('P') == -1 and kydoo_hydro(seq[i:i+11]) >= 2: tmemb = True
	if tmemb is True: print(f'>{defline}')

# python3 65transmembrane.py ../MCB185/data/GCF_000005845.2_ASM584v2_protein.faa.gz
