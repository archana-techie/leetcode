def missing_number(nums):
    nums.sort()
    for i in range(len(nums)):
        if 0 not in nums:
            return 0
        if nums[i] + 1 not in nums:
            return nums[i] + 1

    # or

    
    # c = 0
    # for i in range(1, len(nums) + 1):
    #     c += i
    # s = sum(nums)
    # return c - s


print(missing_number([0,1,2]))