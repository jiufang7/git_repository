class Solution:
    def rob(self, nums):
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        else:
            dp = [0] * len(nums)
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])
            for i in range(2, len(nums)):
                dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        return dp[-1]

if __name__ == '__main__':
    s = Solution()
    rob = s.rob([2,7,9,3,1])
    print(rob)

# 2020.11.9
# dp[i] = max(dp[i-1], dp[i-2] + nums[i]); 其中，dp[i-1]为不偷，dp[i-2] + nums[i]为偷。
# 最后是边界处理，dp[0],dp[1] dp[0]为nums[0]。 dp[1]为max(nums[1], nums[0])