def thirdMax(nums):
    nums = list(set(nums))
    nums.sort()
    if len(nums) < 3:
        return max(nums)
    nums.remove(max(nums))
    nums.remove(max(nums))
    return max(nums)


print(thirdMax([3,4,3,2,4]))