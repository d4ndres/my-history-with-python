
from objeto_para_modulos import Auto

if __name__ == '__main__':
	print( __name__ )

	my_car = Auto(is_turn_on = True)
	while True:
		print(''' 
	
			Comandos:
			[e] nceder
			[a] pagar
			[s] alir

			''')
		command = str(input('Seleccione un comando: '))
		
		if command == 's':
			break
		elif command == 'e':
			my_car.turn_on()
		else:
			my_car.turn_off()

	