#
# Co-Authors: Ashley, Aman

a = 0
b = 1
for i in range(9):
	c = a + b
	a = b
	b = c
	print(a)