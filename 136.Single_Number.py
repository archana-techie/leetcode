

def singleNumber(nums):
    d = {}
    for n in nums:
        if n not in d:
            d[n] = 1
        else:
            d.pop(n)

    return list(d.keys())[0]

    # or
    # return 2 * sum(set(nums)) - sum(nums)


print(singleNumber([1,2,3,2,1]))

