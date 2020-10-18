class Solution:
    def maxArea(self, height):
        s_max = 0
        right = len(height) - 1
        left = 0
        while(left != right):
            temp = (right - left) * min(height[left], height[right])
            if height[left] < height[right]:
                left = left + 1
            else:
                right = right - 1
            if temp > s_max:
                s_max = temp
        return s_max   
        

if __name__ == '__main__':
    s = Solution()
    maxArea = s.maxArea([1,8,6,2,5,4,8,3,7])
    print(maxArea)

# 2020.6.16 
# 最简单的暴力破解复杂度n^2会超时
# 双指针指向列表的头尾，每次计算之后移动数字较小的指针