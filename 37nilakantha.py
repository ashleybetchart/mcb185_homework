# 37 nilakantha by Ashley Betchart
# Co-author: Ashley, Aman

import math

pi = 3
n = 2
sign = 1
for i in range(10):
	pi = pi + (sign) * (4 / (n * (n+1) * (n+2)))
	n = n + 2
	sign = sign * (-1)
	print(pi)