class Solution(object):
    def countBits(self, num):
        """ 
        1: 0001     3:  0011      0: 0000
        2: 0010     6:  0110      1: 0001
        4: 0100     12: 1100      2: 0010 
        8: 1000     24: 11000     3: 0011
        16:10000    48: 110000    4: 0100
        32:100000   96: 1100000   5: 0101
        
        由上可见：
        1、如果 i 为偶数，那么f(i) = f(i/2) ,因为 i/2 本质上是i的二进制左移一位，低位补零，所以1的数量不变。
        2、如果 i 为奇数，那么f(i) = f(i - 1) + 1， 因为如果i为奇数，那么 i - 1必定为偶数，而偶数的二进制最低位一定是0，
        那么该偶数 +1 后最低位变为1且不会进位，所以奇数比它上一个偶数bit上多一个1，即 f(i) = f(i - 1) + 1。
        :type num: int
        :rtype: List[int]
        """
        ret = [0] * (num + 1)
        for i in range(1, num + 1):
            if i % 2 == 0: # 偶数
                #ret.append(ret[i/2])
                ret[i] = ret[i//2] # i/2就会变成float 要用i//2
            else: # 奇数
                #ret.append(ret[i-1] + 1)
                ret[i] = ret[i-1] + 1
        return ret

if __name__ == '__main__':
    s = Solution()
    coinChange = s.countBits(5)
    print(coinChange)

# 2020.11.4