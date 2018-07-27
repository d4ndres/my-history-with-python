# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

#v- 1
# def _is_prime(num):
# 	for idx in range(2, num):
# 		if num % idx == 0:
# 			return False
# 	return True


# if __name__ == '__main__':

# 	result = 0
# 	number = 1

# 	while number != 2000000:
# 		number += 1

# 		if _is_prime(number):

# 			result +=number
# 			print('vas en {}, la suma va [{}]'. format(number, result))

#142913828922
#-------------------------------------------------------------------------
# var start = new Date().getTime();//count the time it takes for the program to run

# var prime = new Array(2,3);//your collection of prime numbers

# //this program will only divide the number you are checking by prime numbers in your collection.
# //this is why it is so fast.
# for(i = 5, ii = 1000; i <= ii ; i++)
# 	{
# 	for ( j = 0 , jj = prime.length ; j < jj ; j++ )
# 		{
# 			if( i % prime[j] == 0)//check for an integer
# 			{
# 				break;
# 			}
# 			else if( j == jj-1)
# 			{
# 				prime[jj] = i;//push number into array prime
# 				console.log(prime[jj]); 
# 			}
# 		}
# }
# var end = new Date().getTime();//stop counting
# var time = end - start;//get the delta time for the count
# console.log('Execution time: ' + time);//display program duration
# for(k = 0, kk = prime.length ; k < kk ; k++)
# {
# 	console.log(prime[k]);//log your collection of prime numbers
# }
# //https://www.codecademy.com/es/forum_questions/51671e51f71c52c3bb0002ed



def write_it( something ):
	with open ('./data_project_euler_py/10_data.txt', 'a') as f:
		f.write( str(something) + '\n' )

def sum_list( one_list ):
	result = 0
	for i in one_list:
		result += i
	return result

def get_prime_list(_max):
	prime_list = [2,3]

	for idx in range( 5, _max):
		print(idx)
		for jdx in range(len(prime_list)):

			if idx % prime_list[ jdx ] == 0:
				break
			elif jdx == len(prime_list) - 1:
				prime_list.append(idx)
	return prime_list


if __name__ == '__main__':
	_max = 2000000

	prime_list = get_prime_list(_max)
	write_it(prime_list)


	result = sum_list( prime_list )

	print(result)