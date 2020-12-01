class Solution:
    def maxProfit(self, prices, fee):
        n = len(prices)
        if n < 2:
            return 0
        dp1 = [0 for _ in range(n)] #第i天手上有股票时的最大收益
        dp2 = [0 for _ in range(n)] #第i天手上无股票时的最大收益
        dp1[0] = -prices[0] #第0天手上有股票的话就是买入prices[0],收益为-prices[0]
        for i in range(1,n):
            dp1[i] = max(dp1[i-1], dp2[i-1] - prices[i]) #保持空,或者买入股票
            dp2[i] = max(dp2[i-1], dp1[i-1] + prices[i] - fee) #保持持有,或者卖掉股票
        return dp2[n-1]

if __name__ == '__main__':
    s = Solution()
    maxProfit = s.maxProfit([1, 3, 2, 8, 4, 9], 2)
    print(maxProfit)

# 2020.12.1
