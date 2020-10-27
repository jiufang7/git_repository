class Solution:
    def wordBreak(self, s, wordDict) :
        if not s:
            return True
        bp = [0] #从0的位置开始匹配
        for i in range(len(s) + 1):
            for j in bp: #从上一次完全匹配的末尾开始匹配
                if s[j : i] in wordDict:
                    bp.append(i) # 找到字典中的单词后，返回最后一位的索引
                    break
        return bp[-1] == len(s) #如果最后一位刚好等于长度，说明完全匹配

# 2020.10.27