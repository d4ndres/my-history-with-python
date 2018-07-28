


def palindrome(word):
	reversed_word = word[::-1]

	if word == reversed_word:
		return True
	return False

def polindrome2(word):
	reversed_word = []

	for letter in word:
		reversed_word.insert(0,letter)

	reversed_word = ''.join(reversed_word)

	if reversed_word == word:
		return True
		
	return False






if __name__ == '__main__':
	word = str(input('Digite una palabra: '))
	result = palindrome(word)
	
	if result is True:
		print('La palabra {} es palindroma'. format(word))
	else:
		print('La palabra {} no es palindroma'. format(word))
