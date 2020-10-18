class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False #负数没有回文数
        str_x = str(x)
        str_x = str_x[::-1] #对字符串进行逆序
        a = int(str_x)
        if a == x:
            return True
        else:
            return False

if __name__ == '__main__':
    s = Solution()
    reverse_int = s.isPalindrome(1321)
    print(reverse_int)

#2020.6.4