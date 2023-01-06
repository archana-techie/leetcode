

def intersection_of_two_arrays(nums1, nums2):
    final_res = []
    for n in nums1:
        if n in nums2:
            if n not in final_res:
                final_res.append(n)
    return final_res


print(intersection_of_two_arrays([4,9,5], [9,4,9,8,4]))
