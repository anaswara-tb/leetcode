def red_Set(b):
	d=int(b,2)
	count=0
	while d>1:
		if d%2==0:
			d//=2
			count += 1
		else:
			d=(d+1)//2
			count += 2
	return count	
print(red_Set('1'))
