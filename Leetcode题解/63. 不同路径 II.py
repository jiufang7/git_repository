class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid) :
        #原矩阵版
        height, width = len(obstacleGrid),len(obstacleGrid[0])

        #从上到下，从左到右
        for m in range(height):#每一行
            for n in range(width):#每一列
                if obstacleGrid[m][n]: #如果这一格有障碍物
                    obstacleGrid[m][n] = 0
                else:
                    if m == n == 0: #或if not(m or n)
                        obstacleGrid[m][n] = 1
                    else:
                        a = obstacleGrid[m-1][n] if m!=0 else 0 #上方格子
                        b = obstacleGrid[m][n-1] if n!=0 else 0 #左方格子
                        obstacleGrid[m][n] = a+b
        return obstacleGrid[-1][-1]

# 2020.10.23
# dp[i][j] = dp[i-1][j] + dp[i][j-1] 依旧是这个核心方程
# 只是有障碍物标志的点，dp[i][j] = 0