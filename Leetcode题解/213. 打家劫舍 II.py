class Solution:
    def rob(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        elif n <= 2:
            return max(nums)
        else:
            # 不抢第一个
            dp1 = [0] * n
            dp1[0] = 0
            dp1[1] = nums[1]
            for i in range(2, n):
                dp1[i] = max(dp1[i-1],nums[i] + dp1[i-2])

            # 不抢最后一个
            dp2 = [0] * n
            dp2[0] = nums[0]
            dp2[1] = max(nums[0],nums[1])
            for i in range(2, n-1):
                dp2[i] = max(dp2[i-1],nums[i] + dp2[i-2])
        return max(dp1[n-1],dp2[n-2])

# 2020.11.9
# 其实就是把环拆成两个队列，一个是从0到n-1，另一个是从1到n，然后返回两个结果最大的。