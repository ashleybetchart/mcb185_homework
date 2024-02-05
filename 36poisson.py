# 36 poison by Ashley Betchart
# Co-authors: Ashley, Aman

import math

def probability(n, k):
	return ((n**k) * ((math.e**(-n)))) / math.factorial(k)
print(probability(2, 3))
print(probability(8, 11))
print(probability(33, 45))