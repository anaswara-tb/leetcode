def minimumCost(nums):
    ans = nums[0]
    nums[1:] = sorted(nums[1:])
    return ans + sum(nums[1:3])

print(minimumCost([5, 3, 1, 4, 2])) 