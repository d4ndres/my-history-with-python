# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a**2 + b**2 = c**2
# For example, 3**2 + 4**2 = 9 + 16 = 25 = 52.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
from math import sqrt
from math import floor
_max = 1000


def pythagorean(a,b):
	return sqrt( a*a + b*b )

def run():
	c = 5
	a = 2
	b = 4
	result = 0
	while result != _max:
		b += 1
		if b >= c:
			a += 1
			b = a + 1
		c = sqrt( a*a + b*b )

		result = a + b + c
		print('Valor de a: {}, b: {} ====> {} <==== {}'. format( a, b, floor(c), result ))  
	
	print(a*b*c)
if __name__ == '__main__':
	run()