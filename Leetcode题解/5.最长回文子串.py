class Solution:
    def longestPalindrome(self, s):
        """
        暴力破解,时间复杂度O(n^3)
        :type s: str
        :rtype: str
        """
        """
        max_len, result = float("-inf"), ""
        #float("-inf")是负无穷的意思 float("inf")是正无穷
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                if s[i:j] == s[i:j][::-1]:
                    if j-i > max_len:
                        max_len = j-i
                        result = s[i:j]
        return result
        """

        """
        回文串是中心对称的，所以只要找到回文串的中心，然后向两边扩展即可。
        中心位置要奇偶分开考虑，如果字符串长度是奇数的话，中心就只有一个元素；如果字符串是偶数的话，那么中心是两个元素。
        """
        if not s or len(s) < 1:
            return ""

        def expandAroundCenter(left, right):
            L, R = left, right
            #从中心向外扩散，左右字符应该相同
            while L >= 0 and R <len(s) and s[L] == s[R]:
                L -= 1
                R += 1
            return R - L - 1

        left, right = 0, 0
        for i in range(len(s)):
            len1 = expandAroundCenter(i, i) # 奇数
            len2 = expandAroundCenter(i, i+1) # 偶数
            max_len = max(len1, len2)

            if max_len > right - left:
                left = i - (max_len - 1)//2
                right = i + max_len//2
                
        return s[left:right+1]

if __name__ == '__main__':
    s = Solution()
    reverse_str = s.longestPalindrome("abcbcb")
    print(reverse_str)

#2020.6.9