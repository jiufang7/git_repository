
class Solution:
    def removeDuplicates(self, nums):
        if len(nums) <= 1:
            return len(nums)
        slow = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[slow]:
                slow += 1
                nums[slow] = nums[i]
        return slow + 1


if __name__ == '__main__':
    s = Solution()
    nums=[1,1,2]
    removeDuplicates_int = s.removeDuplicates(nums)
    print(removeDuplicates_int)

#2020.6.5