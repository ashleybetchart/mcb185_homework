# quiz 3 by Ashley Betchart
# Co-Author: Ashley, Aman

import math

pi = 1
n = 1
sign = -1
for i in range(1, 201, 2):
	pi = pi + ((sign) * (1 /(n + 2)))
	n = n + 2
	sign = sign * (-1)
	print(4 * pi)


