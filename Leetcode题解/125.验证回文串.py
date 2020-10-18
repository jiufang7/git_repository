class Solution:
    def isPalindrome(self, s):
        s = ''.join(filter(str.isalnum,s)).lower()
        return s==s[::-1]
        '''
        if s == "":
            return True
        s_list = list(s)
        for i in s:
            if i >= '0' and i <= '9':
                continue
            elif i >= 'a' and i <= 'z':
                continue
            elif i >= 'A' and i <= 'Z':
                continue
            else:
                s_list.remove(i)
        a = ''.join(s_list)    
        a = a.lower() 
        # 因为忽略大小写，所以统一换成小写
        a_reverse = a[::-1]
        if a == a_reverse:
            return True
        else:
            return False
        '''

if __name__ == '__main__':
    s = Solution()
    ispalindrome = s.isPalindrome("A man, a plan, a canal: Panama")
    print(ispalindrome)

# 2020.6.12

# 注释部分是我自己写的代码 超时了
# 验证是否是回文串只考虑数字和字母，忽视大小写
# 想法是想把字符串转换成列表，然后删去里面非数字和字母的字符
# 再把列表合并成字符串，然后统一成小写，比较和逆序是否相同
# a = ''.join(s_list) join方法可以把前面的字符拼接在后面列表的每一个元素之间，组成一个字符串
# a = a.lower() 把a字符串中的大写字母改成小写

# s = ''.join(filter(str.isalnum,s)).lower() 来自网上巨巨
# filter() 函数用于过滤序列，过滤掉不符合条件的元素，返回一个迭代器对象，如果要转换为列表，可以使用 list() 来转换。
# 该接收两个参数，第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判，然后返回 True 或 False，最后将返回 True 的元素放到新列表中。
# str.isalnum() 方法检测字符串是否由字母和数字组成
# 理解的话 就是先用filter函数把字符串中非字母和数字的部分去掉，变成一个列表，然后用join方法把列表拼接成字符串，最后用lower()方法统一成小写