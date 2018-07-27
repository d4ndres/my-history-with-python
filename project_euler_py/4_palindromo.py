# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

n1 = 999
n2 = 999
data = 0

while n2 != 1:
	n1 = 999
	while n1 != 1:
		result = str(n1*n2)

		if result == result[::-1]:
			result = int( result )
			if result > data:
				data = result
				print('n1: {}, n2: {}, result = {}'. format(n1,n2,data))
		n1 = n1 - 1
	n2 = n2 - 1	

	

