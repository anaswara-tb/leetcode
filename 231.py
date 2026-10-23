def isPowerOfTwo(num):
    if num <= 0:
        return False
    return num & (num - 1) == 0
print(isPowerOfTwo(16))