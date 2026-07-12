def binaryGap(n):
        n = str(bin(n)[2:])
        for i in range(len(n-1)):
                if n[i] == '1' :
                        set = n
          
print(binaryGap(5))	
