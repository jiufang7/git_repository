class Solution:
    def fourSum(self, nums, target) :
        n = len(nums)
        res = []
        nums.sort()
        for i in range(n-3):
            if i > 0 and nums[i] == nums[i-1]: #重复元素跳过
                continue
            if nums[i] + 3 * nums[i+1] > target: #由于递增序列，如果当前数加3倍后面的数就大于目标，后面的都可以跳过了
                break
            if nums[i] + 3 * nums[-1] < target: #如当前数加三倍最后的数都小于目标，当前数直接前进
                continue

            for j in range(i+1, n-2):
                if j > i + 1 and nums[j] == nums[j-1]: #重复元素跳过
                    continue
                if nums[j] + nums[i] + 2 * nums[j+1] > target:
                    break
                if nums[j] + nums[i] + 2 * nums[-1] < target:
                    continue

                low = j + 1
                high = n - 1
                while low < high:
                    if nums[i] + nums[j] + nums[low] + nums[high] == target:
                        res.append([nums[i], nums[j], nums[low], nums[high]])
                        low += 1
                        high -= 1
                        while low < high and nums[low] == nums[low-1]: #重复元素跳过
                            low += 1
                        while low < high and nums[high] == nums[high+1]:
                            high -= 1
                    if nums[i] + nums[j] + nums[low] + nums[high] > target:
                        high -= 1
                    if nums[i] + nums[j] + nums[low] + nums[high] < target:
                        low += 1
        return res

# 2020.10.18