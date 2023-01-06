def contains_near_by_duplicate(nums, k):
    d = {}

    for i in range(0, len(nums)):
        if nums[i] not in d:
            d[nums[i]] = i
        else:
            if abs(i - d[nums[i]]) <= k:
                return True
            else:
                d[nums[i]] = i

    return False


print(contains_near_by_duplicate([1,2,3,1,2,3], 2))