

def intersect(nums1, nums2):
    final_res = []
    values = {}
    for i in nums1:
        if i in values:
            values[i]+=1
            continue
        values[i] = 1
    for i in nums2:
        if i in values and values[i]:
            final_res.append(i)
            values[i] -=1
    return final_res


print(intersect([1,2,], [1,1]))