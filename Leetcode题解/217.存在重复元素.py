class Solution:
    def containsDuplicate(self, nums):
        '''
        nums_set = []
        for i in nums:
            if i not in nums_set:
                nums_set.append(i)
            else:
                return True
        return False
        '''
        nums.sort()
        for i in range(0,len(nums)-1):
            if nums[i] == nums[i + 1]:
                return True
        return False

if __name__ == '__main__':
    s = Solution()
    containsDuplicate = s.containsDuplicate([4,2,1,1])
    print(containsDuplicate)

# 2020.6.14
# 注释部分是我自己写的代码，执行超时
# 想法是准备另一个列表B，把A列表里的元素依次存入，如果存入的元素已经在B中存在了，就证明存在重复
# 这样的时间复杂度好像是n^2
# 大佬的方法是先将列表排序，然后前一个和后一个元素比较，这样的复杂度是n