class Solution:
    def largestDivisibleSubset(self, nums):
        if len(nums) <= 1:
            return nums
        n = len(nums)
        nums.sort()
        dp = [[i] for i in nums] # ex.[[1], [2], [4], [7], [8]]
        for i in range(1, n): 
            for j in range(i-1, -1, -1): #j逆序遍历
                if nums[i] % nums[j] == 0:
                    dp[i] = max(dp[j] + [nums[i]], dp[i], key = len) # key= len代表这里比的是长度
        return max(dp, key = len)


if __name__ == '__main__':
    s = Solution()
    largestDivisibleSubset = s.largestDivisibleSubset([1,2,4,7,8])
    print(largestDivisibleSubset)

# 2020.11.27
# 另一个思路 把问题理解成排序之后,求最长等比数列
# 这样的话和413的等差数列划分就分相似了