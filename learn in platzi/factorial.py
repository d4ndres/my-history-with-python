# -*- coding: utf-8 -*-


def factorial(number):
	if number == 0:
		return 1
	return number * factorial(number - 1)


if __name__ == '__main__':
	numero = int(input('\nFactorial de : '))
	result = factorial(numero)
	print(result)
	