# 22 oligotemp by Ashley Betchart
# Coauthors: Ashley, Aman

import math 

def oligotemp (a, c, g, t):
	total = (a + c + g + t)
	if type(a) != int or type(c) != int or type(g) != int or type(t) != int:
		return 'error: must be whole numbers'
	elif a < 0 or c < 0 or g < 0 or t < 0: return 'error: not possible'
	elif total <= 0: return "total of nucleotides must be greater than 0"
	elif total <= 13: return ((a + t) * 2) + ((g + c) * 4)
	elif total >13: return (64 +(41*(g + c - 16.4)/(total)))
	else: return 'error: not possible'
print(oligotemp(15, 23, 50, 20))
print(oligotemp(12.5, 44, 20, 12))
print(oligotemp(-1, -4, 20, 6))
print(oligotemp(2, 3, 4, 1))

	