# 91 translate by Ashley Betchart
# Co-authors: Ashley, Aman

import argparse
import dogma
import mcb185

parser = argparse.ArgumentParser(description='mRNA translator.')
parser.add_argument('file', type=str, help='fasta file of mRNAs')
parser.add_argument('-m', '--min', type=int, default=100,
	help='min protein length [%(default)i]')
parser.add_argument('-a', '--anti', action='store_true', help='examines anti-parallel strand')
arg = parser.parse_args()

def print_row(seq):
	for i in range(0, len(seq), 60):
		print(seq[i:i+60])

for defline, seq in mcb185.read_fasta(arg.file):
	trans = dogma.translate(seq[seq.find('ATG'):])
	if '*' in trans and trans.find('*') + 1 >= arg.min:
		print(f'{defline}')
		print_row(trans[:trans.find('*')])
	if arg.anti:
		anti = dogma.revcomp(seq)
		if 'ATG' in anti:
			revanti = dogma.translate(anti[anti.find('ATG'):])
			if '*' in revanti and revanti.find('*') + 1 >= arg.min:
				print(f'{defline} anti')
				print_row(revanti[:revanti('*')])