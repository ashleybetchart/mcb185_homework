# 24 accuracy by Ashley Betchart
# Co-authors Ashley, Aman

import math

def F1accuracy_score(a, b, c, d): # a: t+, b: f+, c: t-, d: f-
	p = (a / (a + b)) 
	r = (a / (a + d))
	f1 = ((2 * p * r) / (p + r))
	acc = ((a + c) / (a + d + c + b))
	if a > 1 or a < 0: return "value must be between 0 and 1"
	elif b > 1 or b < 0: return "value must be between 0 and 1"
	elif c > 1 or c < 0: return "value must be between 0 and 1"
	elif d > 1 or d < 0: return "value must be between 0 and 1"
	elif f1 > 1 or f1 < 0: return "value must be between 0 and 1"
	return round(f1, ndigits = 3), round(acc, ndigits = 3)
print(F1accuracy_score(0.11, 0.71, 0.54, 0.38)) 
print(F1accuracy_score(0.44, 0.55, 0.32, 0.47))
print(F1accuracy_score(-2, 0.66, 0.34, 1.0))
print(F1accuracy_score(-6, -0.4, -2, -0.34))