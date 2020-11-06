class Solution:
    def integerBreak(self, n) :
        ans = 1
        if  n < 4:
            return n-1
        while n > 4:
            n -= 3
            ans *= 3
        return ans * n

if __name__ == '__main__':
    s = Solution()
    integerBreak = s.integerBreak(5)
    print(integerBreak)

# 2020.11.4