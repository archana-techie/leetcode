def contains_duplicate(nums):
    s = set()
    for n in nums:
        if n in s:
            return True
        else:
            s.add(n)
    return False


print(contains_duplicate([1,2,3,4,1]))
