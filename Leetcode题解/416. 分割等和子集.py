class Solution:
    def canPartition(self, nums):
        target = sum(nums)
        if target % 2 == 1:
            return False
        else:
            target = target // 2
        n = len(nums)
        dp = [[False for _ in range(target + 1)] for _ in range(n + 1)]
        for i in range(n+1):
            dp[i][0] = True
        for i in range(1, n+1):
            for j in range(1, target+1):
                if j - nums[i-1] < 0:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] | dp[i-1][j - nums[i-1]]
        
        return dp[n][target]

if __name__ == '__main__':
    s = Solution()
    canPartition = s.canPartition([1,2,3,5])
    print(canPartition)

''''
2020.11.26
 * @param {number[]} nums
 * @return {boolean}
 * 背包问题：看数组中是否存在加起来为sum/2的数.
 * 背包容量（V） = sum/2
 * 每一个物品只能装一次,如果出现背包中重量等于sum/2则为true else false
 * dp[i]表示能否填满容量为i的背包
 * 状态转移方程为 dp[i] = dp[i-1] || nums[i]+dp[i-nums[j]]
 * 举例:v = sum/2 = 11   nums = [1,5,11,5]  1是true 0 是false
 *          0  1  2  3  4  5  6  7  8  9  10  11
 *  nums[0] 0  1  0  0  0  0  0  0  0  0   0   0
 *  nums[1] 0  1  0  0  0  1  1  0  0  0   0   0
 *  nums[2] 0  1  0  0  0  1  1  0  0  0   0   1
 *  nums[3] 0  1  0  0  0  1  1  0  0  0   0   1
 * 
 * 所以返回true，因为背包中nums[i]的状态都是由上一行决定的因此可以将二维转化为1维数组从尾部开始
'''