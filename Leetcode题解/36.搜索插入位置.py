class Solution:
    def searchInsert(self, nums, target):
        if target > max(nums):
            return len(nums)
        if target < min(nums):
            return 0
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            if nums[i-1] < target and nums[i] > target:
                return i

# 2020.11.18