def maxProfit(prices):
    max_p = 0
    min_p = prices[0]

    for p in range(1, len(prices) -1):
        max_p = max(prices[p] - min_p, max_p)
        min_p = min(prices[p], min_p)

    return max_p


print(maxProfit([7,5,3,2,1]))


#Algorithm to find largest sum of subarray
def kadane_algo(nums):
    g_max = nums[0]
    c_max = nums[0]

    for i in range(1, len(nums) -1):
        c_max = max(nums[i] + c_max, nums[i])
        if c_max > g_max:
            g_max = c_max

    return g_max


print(kadane_algo([-1,2,3,-3]))
