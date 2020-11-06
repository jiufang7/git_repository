class Solution:
    def countNumbersWithUniqueDigits(self, n) :
        dp = [1, 10, 91]
        for i in range(3, n+1):
            dp.append(dp[i-1] + (dp[i-1] - dp[i-2]) * (10 - i + 1))
        return dp[n]

# 2020.11.5