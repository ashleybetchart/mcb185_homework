# 55 colorname by Ashley Betchart
# Co-authors: Ashley, Aman

import sys

colorfile = sys.argv[1]
R = int(sys.argv[2])
G = int(sys.argv[3])
B = int(sys.argv[4])

min = 1000				#if d < min(d), the min is now d
hexd = []
with open(colorfile) as fp:
	for line in fp:
		words = line.split('\t')
		color = words[0]
		dec = words[2].split(',')
		r = int(dec[0])
		g = int(dec[1])
		b = int(dec[2])
		print(color + abs(R-r) + abs(G-g) + abs(B-b))  # replace w below d = (abs, rm color)
		d = ^
		if d < mind:
			mind = d
			result = color:
print(result)