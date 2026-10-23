def sortPermutation(nums):
	ans = -1
	for i,x in enumerate(nums):
		if x != i:
			ans &= x
	return 0 if ans == -1 else ans
print(sortPermutation([0,1,3,2]))