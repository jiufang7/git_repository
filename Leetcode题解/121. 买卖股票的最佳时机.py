class Solution:
    def maxProfit(self, prices) :
        min_p, max_p = 99999, 0
        for i in range(len(prices)):
            min_p = min(min_p, prices[i])
            max_p = max(max_p, prices[i] - min_p)
        return max_p


if __name__ == '__main__':
    s = Solution()
    maxProfit = s.maxProfit([7,1,5,3,6,4])
    print(maxProfit)

# 2020.11.9
# 记录【今天之前买入的最小值】
# 计算【今天之前最小值买入，今天卖出的获利】，也即【今天卖出的最大获利】
# 比较【每天的最大获利】，取最大值即可
