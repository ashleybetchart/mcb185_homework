# 74 genefinder by Ashley Betchart
# Co-authors: Ashley, Aman

import mcb185
import sys

size = int(sys.argv[2])
def locate_cds(nt, size):
	cds = {}
	for i in range(1, 4):
		while i < len(seq) - size:
			if seq[i:i+3] == 'ATG':
				for j in range(i+3, len(nt) -2, 3):
					if seq[j:j+3] in ['TAA', 'TAG', 'TGA']:
						if j - i + 3 >= size:
							cds[i+1] = j + 3
						i = j + 3
						break
			else: i += 3
	return cds

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	defline = defline.split(' ')[0]

	forw = locate_cds(seq, size)
	rev = locate_cds(mcb185.anti_seq(seq), size)
	all = {}
	for start, stop in forw.items():
		all[start] = stop
	for start, stop in rev.items():
		all[len(seq) -stop +1] = len(seq) - start + 1
	for start, stop in sorted(all.items(), key=lambda item: item[0]):
		if start in forw: print(f'{defline}\tRefSeq\tCDS\t{start}\t{stop}\t.\t+')
		else: print(f'{defline}\tRefSeq\tCDS\t{start}\t{stop}\t.\t-')

