# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


number = 1
bo = True

while bo:
	count = 0
	for divisor in range(1,21):
		if number % divisor == 0:
			count += 1
			if count > 19:
				print('El numero {} con contador {}'. format(number, count))
				bo = False

				

	number += 1
	