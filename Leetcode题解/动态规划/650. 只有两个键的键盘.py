class Solution:
    def minSteps(self, n): 
        if n == 1:
            return 1 
        dp = [1] * (n+1)
        su = [] #存放以及经过的素数
        for i in range(2, n+1):
            if self.isPrime(i): #对于素数来说,需要的次数就是它本身
                su.append(i)
                dp[i] = i
            else: # 非素数来说 举例dp[8] = dp[2] + dp[4]
                for j in su:
                    if i % j == 0: #找到最小的素因数
                        dp[i] = dp[j] + dp[i // j]
                        break
        return dp[n]
    
    def isPrime(self, n): 
        import math
        if n <= 1: 
            return False
        for i in range(2, int(math.sqrt(n)) + 1): 
            if n % i == 0: 
                return False
        return True

if __name__ == '__main__':
    s = Solution()
    minSteps = s.minSteps(4)
    print(minSteps)

#2020.11.29