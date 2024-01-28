# 20 demo by Ashley Betchart

import math

print ("hello again") # greeting
print(2 **3)
print(5 //2)
print(5 *(2+1))
print(math.sqrt(4))

a = 3						# side of triangle
b = 4						# side of triangle
c = math.sqrt(a**2 + b**2) 	# hypotenuse
print(c)

print(type(a), type(b), type(c))
print(type(a), type(b), type(c), sep=", ")

def pythagoras(a, b):
	c = math.sqrt(a**2 + b**2)
	return c
x = pythagoras(3, 4)
print(x)


def pythagoras(a, b):
	return math.sqrt(a**2 + b**2)
print(pythagoras(3, 4))
print(pythagoras(1,1))

def pythagoras(a, b):
	assert(a > 0)
	assert(b > 0)
	return math.sqrt(a**2 + b**2)
print(pythagoras(5, 1))

import sys
def pythagorus(a, b):
	if a <=0: sys.exit('error: a must be greater than 0')
	if b <=0: sys.exit('error: a must be greater than 0')
	return math.sqrt(a**2 + b**2)
print(pythagoras(2,4))