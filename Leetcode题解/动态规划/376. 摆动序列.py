class Solution:
    def wiggleMaxLength(self, nums):
        if len(nums) < 2:
            return len(nums)
        flag = 0 #判断前后差值的标签
        res = 1 #摆动序列长度,最开始为1
        for i in range(1, len(nums)):
            if not flag: #第一次还没有获得差值时
                if nums[i] > nums[i-1]:
                    flag = 1
                    res += 1
                elif nums[i] < nums[i-1]:
                    flag = -1
                    res += 1
            elif (nums[i] - nums[i-1]) * flag < 0: #摆动序列维持
                res += 1
                flag = -flag
        return res

if __name__ == '__main__':
    s = Solution()
    wiggleMaxLength = s.wiggleMaxLength([1,7,4,9,2,5])
    print(wiggleMaxLength)

# 2020.11.26