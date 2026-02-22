def rev_int(n):
	sign = -1 if n < 0 else 1
	n *= sign
	rev = 0
	while n:
		rev = rev * 10 + n % 10
		n //= 10
	return sign * rev	
print(rev_int(-122))  
