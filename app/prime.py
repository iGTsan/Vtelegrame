def is_prime(n):
	for i in range(2, int(n**(1/2)) + 1):
		if n % i == 0:
			return 0
	return 1

def get_prime(n):
	while not is_prime(n):
		n -= 1
	return n