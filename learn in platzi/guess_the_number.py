import random





def run():
	number_found = False
	random_number = random.randint(0 , 20)

	while not number_found:
		number = int(input('Adivina el numero [0-20].\nDigita: '))
		
		if number == random_number:
			print('\nFelicidades has encontrado el numero ${}'. format(random_number))
			number_found = True
		elif number < random_number:
			print('\nOuuu, lo siento el numero es mayor, prueva denuevo ;)')
		else:
			print('\nOuuu, lo siento el numero es menor, prueva denuevo ;)')





if __name__ == "__main__":
	run()