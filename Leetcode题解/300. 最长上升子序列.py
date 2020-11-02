import bisect

class Solution:
    def lengthOfLIS(self, nums):
        if len(nums) <= 1:
            return len(nums)
        dp = [nums[0]]
        for num in nums:
            if num > dp[-1]:
                dp.append(num)
            #    print(dp)
            else:
                loc = bisect.bisect_left(dp, num)
                dp[loc] = num
            #    print(dp)
        return len(dp)

if __name__ == '__main__':
    s = Solution()
    lengthOfLIS = s.lengthOfLIS([10,9,2,5,3,7,101,18])
    print(lengthOfLIS)

'''
2019.11.2

dp[]变化情况
[10]
[9]
[2]
[2, 5]
[2, 3]
[2, 3, 7]
[2, 3, 7, 101]
[2, 3, 7, 18]

bisect 函数其实是 bisect_right 函数的别名，后者还有个姊妹函数叫bisect_left。
bisect_left函数是新元素会被放置于它相等的元素的前面，
而 bisect_right返回的则是跟它相等的元素之后的位置。

做法是二分查找法，新建一个数组，第一个数先放进去，然后第二个数和第一个数比较，如果说大于第一个数，那么就接在他后面，如果小于第一个数，那么就替换。
一般的，如果有i个数，那么每进来一个新的数，都要用二分查找法来得知要替换在哪个位置的数。
因为有个for循环，所以是O(N),在加上循环里有个二分查找，所以最后是O(NlogN)的时间复杂度。
'''