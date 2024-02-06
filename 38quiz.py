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
	pi = 3
	n = 2
	sign = 1
	for i in range(10):
		pi = pi + (sign) * (4 / (n * (n+1) * (n+2)))
		n = n + 2
		sign = sign * (-1)
		print(pi)



pia = 1
na = 1
signa = -1
for i in range(1, 201, 2):
	pia = pia + ((signa) * (1 /(n + 2)))
	na = na + 2
	signa = signa * (-1)
	print(4 * pia)
	pib = 3
	nb = 2
	signb = 1
	for i in range(10):
		pib = pib + (signb) * (4 / (n * (n+1) * (n+2)))
		nb = nb + 2
		signb = signb * (-1)
		print(pib)
