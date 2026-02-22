def aaad(n):
	temp = 0
	while n > 0:
		temp =temp + n % 10
		n //= 10
	return aaad(temp) if temp > 9 else temp
	
print(aaad(38))	