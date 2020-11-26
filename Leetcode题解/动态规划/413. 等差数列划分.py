class Solution:
    def numberOfArithmeticSlices(self, A):
        if len(A) <= 2:
            return 0
        n = len(A)
        dp = [0] * n
        tag = False
        lenth = 3 #表示最长的等差数列长度
        for i in range(2, n):
            if tag == False and A[i] - A[i-1] == A[i-1] - A[i-2]: #刚刚形成等差数列
                tag = True
                dp[i] = dp[i-1] + 1
            elif tag == True and A[i] - A[i-1] == A[i-1] - A[i-2]: #扩大等差数列
                dp[i] = dp[i-1] + lenth - 1
                lenth += 1 #最大等差数列长度增加
            else: #不是等差数列
                dp[i] = dp[i-1]
                tag = False
                lenth = 3
        return dp[-1]
        '''
        还是把问题想复杂了orz
        n=len(A)
        dp=[0]*n
        for i in range(2,n):
            if A[i]-A[i-1]==A[i-1]-A[i-2]:
                dp[i]=dp[i-1]+1
        return sum(dp)
        '''

if __name__ == '__main__':
    s = Solution()
    numberOfArithmeticSlices = s.numberOfArithmeticSlices([1,2,3,4,5,6])
    print(numberOfArithmeticSlices)

# 2020.11.26
# 动态规划的问题
# 迁移方程是如果刚刚形成等差数列 dp[i] = dp[i-1] + 1
# 如果扩大了等差数列           dp[i] = dp[i-1] + lenth - 1 (lenth是之前最大等差数列的长度)
# 如果不是等差数列             dp[i] = dp[i-1]

