# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

number = 600851475143
result = 1

while number > 1:
	result += 1
	while number % result == 0:
		number /= result

print(result)