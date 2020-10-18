class Solution:
    def romanToInt(self, s):
        a = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        ans = 0
        for i in range(len(s)-1): 
            if a[s[i]] >= a[s[i+1]]:
                ans = ans + a[s[i]]
            else:
                ans = ans - a[s[i]]
        ans = ans + a[s[len(s)-1]]
        # 加上最末尾字符所代表的值
        return ans

if __name__ == '__main__':
    s = Solution()
    roma = s.romanToInt("MCMXCIV")
    print(roma)

# 2020.6.29
# 首先建立一个字典来映射符号和值，然后对字符串从左到右来，如果当前字符代表的值不小于其右边，就加上该值；否则就减去该值。
# 以此类推到最左边的数，最终得到的结果即是答案