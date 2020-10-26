class Solution:
    def maxProduct(self, nums) :
        n = len(nums)
        cur_max, cur_min = 1, 1
        res = float("-inf")

        for i in range(n):
            #这里两个变量就是要一起计算的，分开的话cur_max如果发生变化就会产生错误
            cur_max ,cur_min= max(nums[i] * cur_max, nums[i] * cur_min, nums[i]),min(nums[i] * cur_min, nums[i] * cur_max, nums[i])
            res = max(res, cur_max)

        return res

# 2020.10.26