class Solution:
    def reverse(self, x: int) -> int:
        if -10 < x < 10:
    	    return x  #对于个位数的数字，直接输出
        str_x = str(x)
        if str_x[0] != '-':
    	    str_x = str_x[::-1] #将字符串逆序
    	    x = int(str_x)
        else:
    	    str_x = str_x[1:][::-1] #对于有符号的数字，从第二位开始逆序
    	    x = int(str_x)
    	    x = -x
        return x if -2147483648 < x < 2147483647 else 0

if __name__ == '__main__':
    s = Solution()
    reverse_int = s.reverse(-120)
    print(reverse_int)

#2020.6.3