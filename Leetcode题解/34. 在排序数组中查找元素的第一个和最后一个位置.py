class Solution:
    def searchRange(self, nums, target):
        res = [-1,-1]
        if not nums:
            return res
        left = 0
        right = len(nums) - 1
        
        while left < right:
            mid = (left+right) // 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        if nums[left] != target:
            return res
        else:
            res[0] =left
        right = len(nums) - 1 
        while left < right:
            #取右中位数
            mid = (left+right+1) // 2
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid
        res[1] = left 
        return res

# 2020.11.18
# 要求时间复杂度是logn，所以用二分法
# 从中间找到目标，然后往左右两边扩散