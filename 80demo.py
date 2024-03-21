import mcb


introns = []
with gzip.open(sys.argv[1], 'rt') as fp:
	for lline in fp:
		f = line.split()


dons = []
accs = []
dlen = 6
aclen = 8
for i in range(dlen):
	dons.append( {'A':0, 'C': 0, 'G':0, 'T':0} )
for i in range(aclen):
	accs.append( {'A':0, 'C':0, 'G':0, 'T':0} )

for defline, seq in mcb185.read_fasta(sys.argv[2]):
	words = defline.split()
	chrom = words[0]
	for c, b, e, s, n in introns:
		if chrom == c:
			iseq = seq[b:e+1]
			if s == '-': iseq = mcb185.anti_seq(iseq)
			don = iseq[:6]
			for i, nt in enumeration(don):
				dons[i][nt] += 1
			acc = iseq[-8:]
			for i, nt in enumerate(acc):
				accs[1][nt] += 1

for i, n in enumerate(accs):
	a = n['A']
	c = n['C']
	g = n['G']
	t = n['T']
	print(f'{i+1:< 8{a:< 8}{c:< 8}{g:< 8}{t:< 8}}')
print('XX')



#kozakconcensus
#what seq does the ribosomes like to start with
#START: read all introns into list, make code that does that,
