

COUNTRIES = {
	'colombia': 31,
	'argentina': 45,
	'venezuela': 12,
	'peru': 22,
	'ecuador': 55,
	'mexico': 143,
}




while True:
	country = str(input('Ingresa el nombre del pais: ')).lower()

	try:
		print('El numero de  habiantes en {} es de {} millones de habitantes'. format(country , COUNTRIES[country]))
	except KeyError:
		print('Lo sentimos no tenemos el numero de habiantes de {}'.  format(country))
