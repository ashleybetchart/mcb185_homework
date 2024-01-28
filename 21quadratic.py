 # 21 quadratic by Ashley Betchart
 # Coauthors: Ashley, Aman

import math
import sys

def quadratic(a, b, c):
	if (b**2 - (4*a*c)) < 0: sys.exit('error: no real solution')
	else:
		x1 = (-b + math.sqrt(b**2) - (4*a*c)) / (2*a)
		x2 = (-b - math.sqrt(b**2) - (4*a*c)) / (2*a)
	return round(x1, ndigits = 3), round(x2, ndigits = 3)
print(quadratic(3, -3, -9))
print(quadratic(2, 6, -10))
print(quadratic(11, 12, -8))