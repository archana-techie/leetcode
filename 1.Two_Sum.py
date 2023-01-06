def twoSum(nums, target):
    index = {}
    for i in range(len(nums)):
        index[nums[i]] = i

    for i in range(len(nums)):
        second_val = target - nums[i]
        if second_val in index and index[second_val] != i:
            return [i, index[second_val]]


print(twoSum([5,7,2,3,4], 7))