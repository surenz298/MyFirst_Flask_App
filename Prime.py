def isprime(x):
		x = int(x)
		if x == 1:
			return "1 is a special number"
		elif x in [2,3,5]:
			return "is a Prime No!"
		elif x % 2 == 0 or x % 3 == 0 or x % 5 == 0:
			return "is not a Prime No!"
		else:
			max_prime_to_check = int(x ** (1/2.0))
			checkList = []
			while max_prime_to_check > 1:
				checkList.append(x % max_prime_to_check)
				if 0 in checkList:
					return "is not a Prime No!"
				max_prime_to_check -= 1
		return "is a Prime No!"
