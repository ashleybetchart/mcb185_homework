# 84 splicesites by Ashley Betchart
# Co-authors: Ashley, Aman

import sys
import mcb185
import gzip

#can i take out the gff and other part and just input the sys.argv
def print_pwm(pwm, ac, id, de):
	print('AC', ac)
	print('XX')
	print('ID', id)
	print('XX')
	print('DE', de)
	print('P0	A	C	G	T')
	for i, d in enumerate(pwm):
		print(i+1, end='\t')
		for nt, n in d.items():
			print(n, end='\t')
		print()
	print('XX')
	print('//')

chrom = {}
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	chid = defline.split()[0]
	chrom[chid]= seq

introns = []
with gzip.open(sys.argv[2], 'rt') as fp:
	for line in fp:
		f = line.split('\t')
		c = f[0]
		t = f[2]
		b = int(f[3]) -1
		e = int(f[4]) -1
		n = f[5]
		s = f[6]
		if t!= 'intron': continue
		if n == '.': continue
		n = float(n)
		#is there a reason for gap       XXXXXXXXXXXXXXXXX
		introns.append((c, b, e, n, s))

don = []
for i in range(7):
	don.append({'A':0, 'C':0, 'G':0, 'T':0})

acc = []
for i in range(7):
	acc.append({'A':0, 'C':0, 'G':0, 'T':0})

for c, b, e, n, s in introns:
	if s == '+':
		iseq = chrom[c][b:e+1]
	else:
		iseq = mcb185.anti_seq(chrom[c][b:e+1])
		print(iseq[0:6], iseq[-7:], s, n)
	dseq = iseq[0:6]
	for i, nt in enumerate(dseq):
		don[i][nt] +=1
	aseq = iseq[-7:]
	for i, nt in enumerate(aseq):
		acc[i][nt] +=1
print_pwm(acc, 'ap001', 'ACC', 'splice acceptor')
print_pwm(don, 'ap002', 'DON', 'donor site')
"""
fasta = sys.argv[1]
gff = sys.argv[2]

def print_pwm(pwm, ac, id, de):
	print('AC', ac)
	print('XX')
	print('ID', id)
	print('XX')
	print('DE', de)
	print('P0	A	C	G	T')
	for i, d in enumerate(pwm):
		print(i+1, end='\t')
		for nt, n in d.items():
			print(n, end='\t')
		print()
	print('XX')
	print('//')

chrom = {}
for defline, seq in mcb185.read_fasta(fasta):
	chid = defline.split()[0]
	chrom[chid]= seq

introns = []
with gzip.open(gff, 'rt') as fp:
	for line in fp:
		f = line.split('\t')
		c = f[0]
		t = f[2]
		b = int(f[3]) -1
		e = int(f[4]) -1
		n = f[5]
		s = f[6]
		if t!= 'intron': continue
		if n == '.': continue
		n = float(n)
		
		introns.append((c, b, e, n, s))

don = []
for i in range(7):
	don.append({'A':0, 'C':0, 'G':0, 'T':0})

acc = []
for i in range(7):
	acc.append({'A':0, 'C':0, 'G':0, 'T':0})

for c, b, e, n, s in introns:
	if s == '+':
		iseq = chrom[c][b:e+1]
	else:
		iseq = mcb185.anti_seq(chrom[c][b:e+1])
		print(iseq[0:6], iseq[-7:], s, n)
	dseq = iseq[0:6]
	for i, nt in enumerate(dseq):
		don[i][nt] +=1
	aseq = iseq[-7:]
	for i, nt in enumerate(aseq):
		acc[i][nt] +=1
print_pwm(acc, 'ap001', 'ACC', 'splice acceptor')
print_pwm(don, 'ap002', 'DON', 'donor site')
"""