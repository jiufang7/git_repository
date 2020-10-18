class Solution:
    def countAndSay(self, n: int) -> str:
        s = ["1","11"]
        for i in range(2,n):
            ans = ''
            count = 1
            temp = s[i-1] + '-'
            # 加上一个末尾方便后面的j+1处理
            for j in range(len(temp) - 1):
                if temp[j] == temp[j+1]:
                    count = count + 1
                else:
                    ans = ans + str(count) + temp[j]
                    # 拿"11""距离的话，最后count = 2 ，按照加分就变成了 ''+'2'+'1'='21'
                    count = 1
            s.append(ans)
        return s[n-1]

if __name__ == '__main__':
    s = Solution()
    count = s.countAndSay(1)
    print(count)              

# 2020.7.1
# 虽然题目不说人话，但是意思是统计每个字符串中连续相同数字的个数

            