# 83 kozak by Ashley Betchart
# Co-authors: Ashley, Aman

import sys
import mcb185
import gzip

with gzip.open(sys.argv[1], 'rt') as fp:
	complete = []
	coord = []
	seqs = False
	for line in fp:
		line = line.rstrip()
		if line.startswith('VERSION'):
			line = line.split()
			ac = line[1]
		elif line.startswith('     CDS'):
			if 'join' in line: continue
			elif 'complement' in line:
				startid = line.find('(') + 1
				stopid = line.find(')')
				start, stop = line[startid:stopid].split('..')
				coord.append((int(start), int(stop), '-'))
			else:
				start, stop = line.split()[1].split('..')
				coord.append((int(start), int(stop), '+'))
		elif line.startswith('ORIGIN'):
			seqs = True
			continue
		if '/organism=' in line:
			line = line.replace('"','').split('=')
			id = line[1]
		if seqs:
			line = line.split()
			for seq in line[1:]: complete.append(seq)
	complete = ''.join(complete).upper()

kozaks = []
for i in range(14):
	kozaks.append({'A':0, 'C':0, 'G':0, 'T':0})
for start, stop, strd in coord:
	if strd == '-':
		kozak = complete[stop-5:stop+9]
		kozak = mcb185.anti_seq(kozak)
	else:
		kozak = complete[start-10:start+4]
	for i, nt in enumerate(kozak):
		kozaks[i][nt] +=1

print('AC', ac)
print('XX')
print('ID', id)
print('XX')
print('DE PWM for E.Coli')
print('PO	A	C	G	T')
for i, nts in enumerate(kozaks):
	print(f'{i+1:<8}', end='')
	for nt in 'ACGT':
		print(f'{kozaks[i][nt]:<8}', end='')
	print()
print('XX')
print('//')