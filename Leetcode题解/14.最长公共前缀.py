class Solution:
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ""
        strs.sort()
        a = strs[0]
        b = strs[-1]
        # 在经过排序之后，a是字符串中最小的，b是最大的
        common = []
        min_len = min(len(a),len(b))
        for i in range(min_len):
            if a[i] == b[i]:
                common.append(a[i])
            else:
                break
        return "".join(common)
        # common是一个列表，结果返回字符串形式

if __name__ == '__main__':
    s = Solution()
    common = s.longestCommonPrefix(["flower","flow","flight"])
    print(common)

# 2020.6.29
# 在Python里字符串是可以比较的，按照ascII值排，举例abb， aba，abac，最大为abb，最小为aba。所以只需要比较最大最小的公共前缀就是整个数组的公共前缀