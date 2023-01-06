def findDisappearedNumbers(nums):
    res = []
    s = set(nums)
    for i in range(1, len(nums) + 1):
        if i not in s:
            res.append(i)

    return res

print(findDisappearedNumbers([1,2,3,7,8,9]))