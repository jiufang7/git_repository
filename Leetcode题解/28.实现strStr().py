class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        nPos = haystack.find(needle)
        return nPos

if __name__ == '__main__':
    s = Solution()
    npos = s.strStr("aaaaa","")
    print(npos)

#2020.6.10
#str.index()方法如果用来寻找子串，在没有找到时会报错 ValueError: substring not found
#str.find()方法用来寻找子串，没有找到会返回-1，找到就返回第一次找到时的对应索引