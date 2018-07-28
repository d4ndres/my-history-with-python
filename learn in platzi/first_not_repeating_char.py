

"""
"abacabad" c
"abacabaabacaba" _
"abcdefghijklmnopqrstuvwxyziflskecznslkjfabe" d
"bcccccccccccccyb" y
"""

def select_the_first(list_with_tuplas):

	aux = list_with_tuplas[0][0]

	for idx in list_with_tuplas:
		if aux > idx[0]:
			aux = idx[0]
	return aux

def search_char_not_repeat(sequence_of_chars):
	data_char = {}

	for idx, letter in enumerate(sequence_of_chars):

		if letter not in data_char:
			data_char[letter] = (idx, 1)
		else:
			data_char[letter] = (data_char[letter][0] , data_char[letter][1] + 1)


	del_data_char = []

	for key, value in data_char.items():

		if value[1] == 1:
			del_data_char.append(data_char[key])


	
	if del_data_char == []:
		return '_'
	else:
		position = select_the_first(del_data_char)
		return sequence_of_chars[position]




if __name__ == '__main__':
	sequence_of_chars = str(input('Digita una secuencia de caracteres: '))


	result = search_char_not_repeat(sequence_of_chars)

	if result == '_':
		print('Todos los caracteres en la secuencia se repiten')
	else:
		print('El primer caracter en no repetirce es : {} ', format(result))