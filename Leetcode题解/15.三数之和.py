class Solution:
    def threeSum(self, nums):
        '''
        nums.sort()
        first = 0
        last = len(nums)-1
        res = []

        if len(nums) < 3:
            return res

        def FindOne(first,last,nums):
            temp = []
            for i in range(first + 1,last):
                if nums[first] + nums[i] + nums[last] == 0:
                    temp.append(nums[first])
                    temp.append(nums[i])
                    temp.append(nums[last])
                    return temp
            return temp

        def FindMore(first,last,nums):
            for x in range(first + 1,last)[::-1]:
                for y in range(x + 1,last)[::-1]:
                    if nums[x] + nums[y] > nums[last]:
                        return False
            return True

        while first < last:
            temp = []
            temp = FindOne(first,last,nums)
            if temp:
                if temp not in res:
                    res.append(temp)
                while last > first and nums[last] == nums[last-1]:
                    last = last - 1
                last = last - 1   
            else:
                if nums[first] + nums[last] < 0 and FindMore(first,last,nums):
                    while last > first and nums[first] == nums[first + 1]:
                        first = first + 1
                    first = first + 1
                    last = len(nums) - 1
                else:
                    while last > first and nums[last] == nums[last-1]:
                        last = last - 1
                    last = last -1

        return res
        '''
        nums.sort()
        res =[]
        i = 0
        for i in range(len(nums)):
            if i == 0 or nums[i]>nums[i-1]:
                # num[i]>nums[i-1]用来去重复，一样的数字就不判断了
                l = i+1
                r = len(nums)-1
                # l,r双指针
                while l < r:
                    s = nums[i] + nums[l] + nums[r]
                    if s ==0:
                        res.append([nums[i],nums[l],nums[r]])
                        l +=1
                        r -=1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                        while r > l and nums[r] == nums[r+1]:
                            r -= 1
                        # 上面两个while用于去重复，删掉相同元素
                    elif s>0:
                        r -=1
                    else :
                        l +=1
        return res

if __name__ == '__main__':
    s = Solution()
    three = s.threeSum([-4,-1,-4,0,2,-2,-4,-3,2,-3,2,3,3,-4])
    print(three)

# 2020.6.30
# 注释部分是自己写的代码，最后超时了orz   