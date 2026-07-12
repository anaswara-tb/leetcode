def conca_bin(n):
    result = ""
    for i in range(1,n+1):
        result += bin(i)[2:]  
    return int(result,2)%1000000007


print(conca_bin(12))  