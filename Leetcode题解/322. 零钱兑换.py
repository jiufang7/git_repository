class Solution:
    def coinChange(self, coins, amount) :
        if coins and amount == 0:
            return 0
        counts = [0] * (amount + 1)
        for i in range(1, amount+1):
            cost = float("inf")
            for j in coins:
                if i - j >= 0:
                    cost = min(cost, counts[i-j]+1)
                    #print(i, j , cost)
            counts[i] = cost
        #print(counts)
        return counts[-1] if counts[-1] != float("inf") else -1 


if __name__ == '__main__':
    s = Solution()
    coinChange = s.coinChange([1,2,5], 11)
    print(coinChange)

# 2020.11.3
'''
再具体解释一下这个公式吧，例如这个示例：

输入: coins = [1, 2, 5], amount = 11
输出: 3 
解释: 11 = 5 + 5 + 1
题目求的值为 f(11)，第一次选择硬币时我们有三种选择。

假设我们取面额为 1 的硬币，那么接下来需要凑齐的总金额变为 11 - 1 = 10，即 f(11) = f(10) + 1，这里的 +1 就是我们取出的面额为 1 的硬币。

同理，如果取面额为 2 或面额为 5 的硬币可以得到：

f(11) = f(9) + 1
f(11) = f(6) + 1
所以：

f(11) = min(f(10), f(9), f(6)) + 1

'''