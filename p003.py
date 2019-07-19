import math

def checkPrime(n):
	i = 2
	if n == 2 or n == 3:
		return True
	while i ** 2 <= n:
		if n % i == 0:
			return False
		i += 1
	return True
	
prime = 600851475143
sqrt = math.ceil(math.sqrt(prime))
for i in range(2, sqrt):
	if(prime % i == 0):
		print('i: ' + str(i) + ' i_inverse: ' + str(prime/i) + ' isPrime: ' + str(checkPrime(int(i))) + ', ' + str(checkPrime(int(prime/i))))
