# The sum of the squares of the first ten natural numbers is,

# 12 + 22 + ... + 102 = 385
# The square of the sum of the first ten natural numbers is,

# (1 + 2 + ... + 10)2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def sum_of_squares(lim):
	_sum = 0
	for idx in range( 1,lim + 1):
		_sum += (idx*idx)
	return _sum

def square_of_sum(lim):
	_sum = 0
	for idx in range( 1, lim + 1):
		_sum += idx

	return _sum*_sum




if __name__ == '__main__':

	number = int(input('Digite el limite: '))
	sums = sum_of_squares( number)
	ssum = square_of_sum( number )
	result = ssum - sums
	print('the difference between {} - {} = {}'. format( ssum, sums,result))