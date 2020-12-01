class Solution:
    def maxSumDivThree(self, nums):
        min_1, min_2 = float("inf"), float("inf")
        min_3, min_4 = float("inf"), float("inf")
        res = 0
        for num in nums:
            res += num
            if num % 3 == 0:
                continue
            elif num % 3 == 1: #min1,min2存放被3除余1的,两个最小值,min1更小
                if num < min_1:
                    min_1, min_2 = num, min_1
                elif num < min_2:
                    min_2 = num
            else: #min3,min4存放被3除余2的,两个最小值,min3更小
                if num < min_3:
                    min_3, min_4 = num, min_3
                elif num < min_4:
                    min_4 = num
        if res % 3 == 0:
            return res
        elif res % 3 == 1:
            return res - min(min_1, min_3 + min_4) #min3和min4相加也是余1
        else:
            return res - min(min_3, min_1 + min_2) #min1和min2相加也是余2

# 2020.11.30