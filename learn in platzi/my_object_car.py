from random import randint as range_rand


class Car:

	_ESTADO = ['''
                    _______
                  _/\______\\__
                 / ,-. -|-  ,-.`-.
                 `( o )----( o )-'
                   `-'      `-''','''
                    _______
                  _/\______\\__
                 / ,-. -|-  ,-.`-.
            -  --`( o )----( o )-'
                   `-'      `-''',
                    '''
                    _______
            _-_-  _/\______\\__
         _-_-__  / ,-. -|-  ,-.`-.
            _-_- `( o )----( o )-'
                   `-'      `-'''
    ]


	def __init__(self):
		self._is_turn_on = False
		self._speed  = 0
		self._show_car()

	def turn_on(self):
		self._is_turn_on = True
		self._show_car()

	def turn_off(self):
		self._is_turn_on = False
		self._show_car()

	def speed(self, initial_speed = 0):
		self._speed = initial_speed + self._speed +1
		self._show_car() 

	def _show_car(self):

		if self._is_turn_on == False:
			print(self._ESTADO[0])
		else:
			if self._speed > 0:
				print(self._ESTADO[2])
			else:
				print(self._ESTADO[1])






def run():

	my_car = Car() 

	while True:

		if my_car._is_turn_on == False:
			print(''' 
	
			Comandos:
			[e]nceder
			[s]alir

			''')
		else:
			print(''' 
	
			Comandos:
			[a]celerar
			a[p]pagar
			[s]alir

			''')


		
		command = str(input('Seleccione un comando: '))
		
		if command == 's':
			break
		if command == 'e':
			my_car.turn_on()
		if command == 'a':
			my_car.speed()
		if command == 'p':
			my_car.turn_off()



if __name__ == '__main__':
	print('\t\tSIMULADOR DE AUTOS')
	run()
	