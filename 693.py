def hasAlternatingBits(n):
        n = str(bin(n)[2:])
        for i in range(len(n) - 1):  
            if n[i] == n[i+1]:
                return False
        return True  
print(hasAlternatingBits(5))	
