class Solution:
    def numSquares(self, n: int) :
        dp = [0] * (n+1)
        for i in range(1, n+1):
            val = i
            j = 1
            while i - j * j >= 0:
                val = min(val, dp[i-j*j] + 1)
                j += 1
            dp[i] = val
        return dp[n]

if __name__ == '__main__':
    s = Solution()
    numSquares = s.numSquares(12)
    print(numSquares)