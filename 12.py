"""
def int_to_r(num):
	str = []
	while(num<0):
		num = num%1000
		str = [num//1000 * "M"] +str
		if(num<500):
			str = [num//500 * "D"] +str
			num = num%500
			if(num<100):
				str = [num//100 * "C"] +str
				num = num%100
				if(num<50):
					str = [num//50 * "L"] +str
					num = num%50
					if(num<10):
						str = [num//10 * "X"] +str
						num = num%10
						if(num<5):
							str = [num//5 * "V"] +str
							num = num%5
							str = [num * "I"] +str
	return (str)
int_to_r(1234)
"""
def int_to_roman(num):
    values = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"),  (90, "XC"),  (50, "L"),  (40, "XL"),
        (10, "X"),   (9, "IX"),   (5, "V"),   (4, "IV"),
        (1, "I"),
    ]

    result = []
    for value, symbol in values:
        count = num // value      # how many of this symbol fit
        result.append(symbol * count)
        num %= value              # what's left to convert

    return "".join(result)


print(int_to_roman(1234))   # MCCXXXIV
print(int_to_roman(4))      # IV
print(int_to_roman(9))      # IX
print(int_to_roman(49))     # XLIX
print(int_to_roman(1994))   # MCMXCIV
print(int_to_roman(3999))   # MMMCMXCIX