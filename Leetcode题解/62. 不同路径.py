class Solution:
    def uniquePaths(self, m: int, n: int) :
        dp = [[0 for _ in range(n)] for _ in range(m)] #构建二维数组的方法
        dp[0][0] = 0
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1

        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[-1][-1]

# 2020.10.23
# 今天开始做动态规划问题
# dp[i][j] = dp[i-1][j] + dp[i][j-1]  核心的动态规划方程