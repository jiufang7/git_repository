class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1 or x == 2 or x == 3:
            return 1
        for i in range(int(x/2)+2): #这里+2是因为如果+1的话5是错误的
            if i*i == x :
                return i
            elif i*i > x :
                return i-1
            else:
                continue

if __name__ == '__main__':
    s = Solution()
    sqrt_int = s.mySqrt(5)
    print(sqrt_int)

#2020.6.8