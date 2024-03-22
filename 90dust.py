# 90 dust by Ashley Betchart
# Co-authors: Ashley, Aman

import math
import mcb185
import argparse

parser = argparse.ArgumentParser(description='DNA entropy filter.')
parser.add_argument('file', type=str, help='name of fasta file')
parser.add_argument('-s', '--size', type=int, default=20,
	help='window size [%(default)i]')
parser.add_argument('-e', '--entropy', type=float, default=1.4,
	help='entropy threshold [%(default).3f]')
parser.add_argument('--lower', action='store_true', help='soft mask')
arg = parser.parse_args()

w = int(arg.size)
e = float(arg.entropy)
for defline, seq in mcb185.read_fasta(arg.file):
	print(f'>{defline}')
	output = list(seq)
	for i in range(len(seq) -w +1):
		s = seq[i:i+w]
		ent = 0
		if s.count('A') > 0: ent -= s.count('A') / w * math.log2(s.count('A') / w)
		if s.count('C') > 0: ent -= s.count('C') / w * math.log2(s.count('C') / w)
		if s.count('G') > 0: ent -= s.count('G') / w * math.log2(s.count('G') / w)
		if s.count('T') > 0: ent -= s.count('T') / w * math.log2(s.count('T') / w)
		if ent < e:
			if arg.lower is not True:
				for j in range(w):
					output[i+j] = 'N'
			elif arg.lower is True:
				for j in range(w):
					if   seq[i+j] == 'A': output[i+j] = 'a'
					elif seq[i+j] == 'C': output[i+j] = 'c'
					elif seq[i+j] == 'G': output[i+j] = 'g'
					elif seq[i+j] == 'T': output[i+j] = 't'
					elif seq[i+j] == 'N': output[i+j] = 'n'
	num = 0
	for i in output:
		if num == 60:
			print()
			num = 0
		print(i, end='')
		num += 1
	print()