def min_op_sortstr(s):
	count = 0
	if(len(s) <= 2):
		return -1
	for i, char in enumerate(s[:-1]):
    		if char > s[i + 1]:
							
							count +=1
			
	return count
print(min_op_sortstr("dog"))
print(min_op_sortstr("card"))
print(min_op_sortstr("hi"))
print(min_op_sortstr("cab"))


def min_operations(s):
    n = len(s)
    t = sorted(s)

    if list(s) == t:
        return 0
    if n == 2:
        return -1

    l = 0
    while s[l] == t[l]:
        l += 1
    r = n - 1
    while s[r] == t[r]:
        r -= 1

    if l > 0 or r < n - 1:        # a proper window fixes it
        return 1

    if min(s) not in s[:-1] and max(s) not in s[1:]:
        return 3
    return 2

print(min_operations("jgg"))  # 2
print(min_operations("jjg"))  # 2
print(min_operations("cba"))  # 3
print(min_operations("cab"))  # 2
print(min_operations("card")) # 1