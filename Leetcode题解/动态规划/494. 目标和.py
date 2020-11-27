class Solution:
    def findTargetSumWays(self, nums, S):
        target = sum(nums) + S
        if target % 2 == 1 or sum(nums) < S: #对于奇数目标和过大的目标直接返回0
            return 0
        else:
            target = target // 2
        return self.sub_set(nums,target)

    def sub_set(self,nums,target):
        dp = [0]*(target+1) # dp[i]表示target为i有多少种方法
        dp[0] = 1
        for num in nums:
            #每一遍循环得到和值为i的方法数，以次更新
            for i in range(target, num-1, -1):
                dp[i] += dp[i-num] 
        return dp[target] 

'''
2020.11.27
原问题等同于： 找到nums一个正子集和一个负子集，使得总和等于target

我们假设P是正子集，N是负子集 例如： 假设nums = [1, 2, 3, 4, 5]，target = 3，一个可能的解决方案是+1-2+3-4+5 = 3 这里正子集P = [1, 3, 5]和负子集N = [2, 4]

那么让我们看看如何将其转换为子集求和问题：

sum(P) - sum(N) = target
sum(P) + sum(N) + sum(P) - sum(N) = target + sum(P) + sum(N)
2 * sum(P) = target + sum(nums)

因此，原来的问题已转化为一个求子集的和问题： 找到nums的一个子集 P，使得sum(P) = (target + sum(nums)) / 2
'''