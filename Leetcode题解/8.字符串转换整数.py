class Solution(object):
  def myAtoi(self, s):
    """
    :type str: str
    :rtype: int
    """
    s = s.strip()
    # s.strip()可以把字符串前后两端的空格去掉
    sign = 1

    if not s:
      return 0
    # 对于只由空格组成的字符串还有空字符串来说，s.strip()之后一定是空字符串

    if s[0] in ["+", "-"]:
      if s[0] == "-":
        sign = -1
      s = s[1:]
    # 取正负号，然后从字符串第二位开始计数

    ans = 0
    for c in s:
      if c.isdigit():
        ans = ans * 10 + int(c)
      else:
        break
    # c.isdigit()判断字符是不是数字

    ans *= sign
    if ans > 2147483647:
      return 2147483647
    if ans < -2147483648:
      return -2147483648
    return ans     

if __name__ == '__main__':
    s = Solution()
    atoi_int = s.myAtoi("-hjkfd2")
    print(atoi_int)

# 2020.6.28