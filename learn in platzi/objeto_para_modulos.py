
print( __name__ )

class Auto:

	_Estado = ['''
                    _______
                  _/\______\\__
                 / ,-. -|-  ,-.`-.
                 `( o )----( o )-'
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
		self._show_estado()

	def __init__(self, is_turn_on = False):
			self._is_turn_on = is_turn_on
			self._show_estado()	



	def turn_on(self):
		self._is_turn_on = True
		self._show_estado()

	def turn_off(self):
		self._is_turn_on = False
		self._show_estado()

	def _show_estado(self):
		if self._is_turn_on:
			print(self._Estado[1])
		else:
			print(self._Estado[0])


