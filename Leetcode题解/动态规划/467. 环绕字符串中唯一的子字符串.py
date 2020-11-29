class Solution:
    def findSubstringInWraproundString(self, p):
        if len(p) <=1:
            return len(p)
        from collections import defaultdict
        # default(int)则创建一个类似dictionary对象，里面任何的values都是int的实例
        # 而且就算是一个不存在的key, d[key] 也有一个默认值，这个默认值是int()的默认值0.
        dp = defaultdict(int) 
        dp[p[0]], curMaxLen = 1, 1
        for idx in range(1, len(p)):
            if (ord(p[idx]) - ord(p[idx - 1])) % 26 == 1:
                curMaxLen += 1
            else:
                curMaxLen = 1
            dp[p[idx]] = max(dp[p[idx]], curMaxLen)
            #对于第一次出现的字母,以它为结尾的子串就是curMaxlen
            #对于第二次及之后出现的字母,以它为结尾的子串,如果没有超过原先的,那么都是重复的,需要舍弃
        return sum(dp.values())

# 2020.11.29
# 这里用的是字典,就可以去掉重复的子串
# 因为子串对顺序的要求很严格,同一个字母结尾,一个长度只有一个串.