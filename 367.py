def square(num):
	for i in range(0, num//2 + 1):
		if i*i == num:
			return True	
	return False
print(square(1))