



def binary_search(numbers, number_to_find, low, high):
	
	if low > high:
		return False
	
	mid = int((low + high) / 2)

	print(numbers[mid])
	if numbers[mid] == number_to_find:
		return True
	elif numbers[mid] > number_to_find:
		
		return binary_search(numbers, number_to_find, low, mid - 1)
	else:
		
		return binary_search(numbers, number_to_find, mid + 1, high)
		






if __name__ == '__main__':
	numbers = [ 1,2,3,4,5,6,7,8,9,10,15,20,24,30,34,50]
	print(len(numbers) - 1)

	

	number_to_find = int(input('Digite un numero: '))

	result = binary_search(numbers,number_to_find, 0, len(numbers) - 1)

	if result is True:
		print('El numero si esta en la lista')
	else:
		print('El numero no esta en la lista')