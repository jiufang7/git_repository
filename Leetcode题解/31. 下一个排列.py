class Solution:
    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        
        if len(nums) < 2:
            return
        i = len(nums) - 1
        while i > 0 and nums[i] <= nums[i-1]:
            i -= 1
        a, b = i, len(nums)-1
        while a < b:
            nums[a],nums[b] = nums[b],nums[a]
            a += 1
            b -= 1
        
        j = i-1
        for k in range(i, len(nums)):
            if nums[k] > nums[j]:
                nums[j], nums[k] = nums[k], nums[j]
                break

# 2020.11.16
# 源于离散数学及其应用的算法：（以3 4 5 2 1 为例）
# 从后往前寻找第一次出现的正序对：（找到 4,5）
# 之后因为从5 开始都是逆序，所以把他们反转就是正序：3 4 1 2 5
# 之后4 的位置应该是：在它之后的，比他大的最小值（5）
# 交换这两个值：得到 3 5 1 2 4
# 对于初始即为逆序的序列，将在反转步骤直接完成