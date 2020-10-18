class Solution:
    def singleNumber(self, nums):
        for i in range(1,len(nums)):
            res = nums[0] ^ nums[i]
            nums[0] = res
        return nums[0]

if __name__ == '__main__':
    s = Solution()
    singlenumber = s.singleNumber([4,1,2,1,2])
    print(singlenumber)
            
# 2020.6.13
# 列表中只出现一次的数字
# 想法是把列表里所有的数字用 异或（^） 运算叠加，最后的结果就是只出现一次的数字
# 因为一个数异或本身结果是1