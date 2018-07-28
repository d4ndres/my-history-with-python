
def primo(n):
	if n < 2:
		return False
	elif n == 2:
		return True
	else:
		for i in range(3,n):
			if n % i == 0:
				return False
	return True

def run():
	print('DETECTOR DE NUMEROS PRIMOS')
	print('')
	 num = int(input('Digite un numero: '))
	#for num in range(1, 100):
		result = primo(num)
		if result == True:
			print('El numero {} es primo'. format(num))
		else:
			print('El numero {} No es primo'. format(num))


	return 0;
		

if __name__ == '__main__':
	run()