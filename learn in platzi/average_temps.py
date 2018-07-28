





def average_temps(temps):
	sum_of_temps = 0

	for temp in temps:
		sum_of_temps += float(temp)

	return sum_of_temps / len(temps)






if __name__ == '__main__':
	temps = [23,21,34,32,16,33]

	result = average_temps(temps)

	print(result)