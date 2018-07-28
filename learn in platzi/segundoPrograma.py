# -*- coding: utf-8 -*-


def saludar(n):
	if(n >= 18):
		print('Buen día senior ' + name + '.' )
	else:
		print('hola, ' + name + '!')

if __name__ == '__main__':
	name = str(input('Cual es tu nombre?'))
	edad = int(input('dime tu edad: '))
	saludar(edad)