def segment_one(Str):
	if Str[0] == '1' :
		for i in range(1,len(Str)):
			if Str[i] == '1' and Str[i+1] == '1' :
				return True
			else : 
				return False
	else:		
		return False	
print(segment_one('101'))
	
