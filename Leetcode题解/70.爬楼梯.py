class Solution:
    def climbStairs(self, n):
        res = [0,1,1]
        for i in range(3,n+2):
            res.append(res[i-1] + res[i-2])
        return res[n+1]

if __name__ == '__main__':
    s = Solution()
    climbStairs = s.climbStairs(5)
    print(climbStairs)

# 2020.6.15
# 斐波那契数列