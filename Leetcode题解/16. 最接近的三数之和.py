class Solution:
    def threeSumClosest(self, nums, target) :
        n = len(nums)
        nums.sort()
        re_min = 0 #存储当前最小的差值

        for i in range(n):
            low = i + 1
            high = n - 1
            while low < high:
                three_sum = nums[i] + nums[low] + nums[high]
                x = target - three_sum #当前三个数离目标的值

                if re_min == 0: #第一次初始化
                    re_min = abs(x)
                    sum_min = three_sum #sum_min为当前最接近的和
                
                if abs(x) < re_min: #更为接近的时候
                    re_min = abs(x)
                    sum_min = three_sum
                
                if three_sum == target:
                    return target
                elif three_sum < target:
                    low += 1
                else:
                    high -= 1
        return sum_min

# 2020.10.18