import random

IMAGES = ['''
    +---+
    |   |
        |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
    |   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   /    |
        =========''','''
	 _   _  ___  _   _    __ _ _ __ ___    __| (_) ___ 
	| | | |/ _ \| | | |  / _. | .__/ _ \  / _. | |/ _ \	
	| |_| | (_) | |_| | | (_| | | |  __/ | (_| | |  __/
	 \__. |\___/ \__._|  \__._|_|  \___|  \__._|_|\___|
	 |___/                                             '''
]


WORDS = [
	'comida',
	'fresa',
	'lapiz',
	'fea',
	'monedas',
	'wifi',
	'platzi',
	'libro'
]

def random_word():
	idx = random.randint(0, len(WORDS)-1)
	return WORDS[idx]

def disply_ahorcado(tries , hidden_word):
	print(IMAGES[tries])
	print('')
	print('*************************************************')
	print(hidden_word)
	print('')

def run():
	word = random_word()
	hidden_word = list(('-') * len(word))
	tries = 0
	hit = 0

	while True:
		disply_ahorcado( tries ,hidden_word )
		if tries == len(IMAGES) - 1:
				return print('Has perdido, intentalo otra ves =)')
		elif hit == len(word) :
				return print('En hora buena has ganado')


		guess_letter = str(input('Digita una letra para intentar: '))
		find_letter = word.find(guess_letter)

		if find_letter == -1:
			tries += 1
		else:
			hidden_word[find_letter] = word[find_letter]
			hit += 1

			

			


if __name__ == '__main__':
	print('\tHI, ESTO ES AHORCADOS')
	run()