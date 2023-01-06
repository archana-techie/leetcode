def move_zeroes(nums):
    for i in range(len(nums)):
        if nums[i] == 0:
            nums.remove(nums[i])
            nums.append(0)
    return nums


print(move_zeroes([0,1,2,3,4,0]))