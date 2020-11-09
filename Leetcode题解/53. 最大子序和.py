class Solution:
    def maxSubArray(self, nums):
        for i in range(1, len(nums)):
            nums[i]= nums[i] + max(nums[i-1], 0)
            #print(nums[:i])
        return max(nums)

if __name__ == '__main__':
    s = Solution()
    maxSubArray = s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
    print(maxSubArray)

# 2020.11.9
# 思想是动态规划，nums[i-1]并不是数组前一项的意思，而是到前一项为止的最大子序和，和0比较是因为只要大于0，就可以相加构造最大子序和。
# 如果小于0则相加为0，nums[i]=nums[i]，相当于最大子序和又重新计算。其实是一边遍历一边计算最大序和