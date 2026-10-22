def min_operations(nums):
    n = len(nums)
    p = nums.index(0)              # position of 0

    # Case 1: nums is a rotation of [0, 1, ..., n-1]
    if all(nums[(p + j) % n] == j for j in range(n)):
        if p == 0:
            return 0
        return min(p, n - p + 2)

    # Case 2: nums is a rotation of the reversed sorted array
    rev = nums[::-1]
    q = n - 1 - p                  # position of 0 in the reversed array
    if all(rev[(q + j) % n] == j for j in range(n)):
        return min(1 + q, (p + 1) % n + 1)

    return -1

print(min_operations([0, 2, 1]))     # -1
print(min_operations([1, 2, 0]))     # 2
print(min_operations([2, 1, 0]))     # 1
print(min_operations([0, 1, 2]))     # 0
print(min_operations([1, 0, 3]))     # -1
print(min_operations([2, 0, 1, 3]))  # -1