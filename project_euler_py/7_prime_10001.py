# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?

def _is_prime(num):
	for idx in range(2, num):
		if num % idx == 0:
			return False
	return True


if __name__ == '__main__':

	value = 0
	number = 1

	while value != 10001:
		number += 1

		if _is_prime(number) is True:
			value += 1
			print('idx[{}] ====> value: {}'. format(value, number))

	print('idx[{}] ====> value: {}'. format(value, number))



