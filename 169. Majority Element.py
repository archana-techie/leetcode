def majority_elem(nums):
    # d = {}
    # for n in nums:
    #     if n not in d:
    #         d[n] = 1
    #     else:
    #         d[n] += 1
    # max_elem_num = max_elem = 0
    # for n in d:
    #     if d[n] > max_elem:
    #         max_elem = d[n]
    #         max_elem_num = n
    # return max_elem_num


    #or
    count = 0
    major_elem = 0
    for n in nums:
        if count == 0:
            major_elem = n
            count = 1

        else:
            if n == major_elem:
                count+=1
            else:
                count-=1

    return major_elem


print(majority_elem([1,2,3,4,1,1,4,4,5]))