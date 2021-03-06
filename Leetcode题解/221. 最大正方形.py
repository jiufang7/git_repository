class Solution:
    def maximalSquare(self, matrix) :
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * (n+1) for _ in range(m+1)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                if matrix[i-1][j-1] == '1':
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
        
        return max(map(max, dp)) ** 2

'''
2020.11.1

dp[i][j]表示以第i行第j列为右下角所能构成的最大正方形边长, 则递推式为: 
dp[i][j] = 1 + min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]);
   
'''