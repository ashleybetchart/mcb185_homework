# 25 entropy
# Co-authors: Ashley, Aman

import math

def entropy (a, c, g, t):
	tnt = (a + c + g + t)
	pa = (a / tnt)
	pc = (c / tnt)
	pg = (g / tnt)
	pt = (t / tnt)
	if type(a) != int or type(c) != int or type(g) != int or type(t) != int: 
		return "error: must be whole numbers"
	elif a < 0 or c < 0 or g < 0 or t < 0:
		return "error: nt cannot be negative"
	else: 
		return -(pa * math.log2(pa) + pc * math.log2(pc) + pg * math.log2(pg) + pt * math.log2(pt))
print(entropy(3, 5, 3, 7))
print(entropy(44, 65, 89, 23))
print(entropy(11, 222, 65, 33))