# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
below = 1000
result = 0
for number in range (2, below ):
	if number % 3 == 0 or number % 5 == 0:
		result += number
		print('number ==> ', number) 

print('El resultado es: ', result) 

