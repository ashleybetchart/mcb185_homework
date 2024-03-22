# 82 transfac by Ashley Betchart
#Co-authors: Ashley, Aman

import json
import re
import sys
import gzip

matrices = []
with gzip.open(sys.argv[1], 'rt') as fp:
	data = ''
	for line in fp:
		if line.split()[0] == 'ID':
			info = line.split()[1]
			data = {'id': info, 'pwm': []}

		if re.search('[0123456789]', line.split()[0]):
			n, a, c, g, t = line.split()
			a = float(a)
			c = float(c)
			g = float(g)
			t = float(t)
			counts = {'A': a, 'C': c, 'G': g, 'T': t}
			data['pwm'].append(counts)
		if data: matrices.append(data)
print(json.dumps(matrices, indent=4))