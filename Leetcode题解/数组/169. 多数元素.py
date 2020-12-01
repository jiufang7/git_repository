class Solution:
    def majorityElement(self, nums):
        from collections import Counter
        return Counter(nums).most_common(1)[0][0]
        # most_common(n)就是输出出现次数最n多的那些元素,格式是一个列表,列表元素是一个二元组
        # Counter(nums).most_common(1) 输出[(3,2)]
        # Counter(nums).most_common(1)[0] 输出(3,2)
        # Counter(nums).most_common(1)[0][0] 输出3
        '''
        nums.sort()
        return nums[int(len(nums)/2)]
        '''

        

if __name__ == '__main__':
    s = Solution()
    majorityElement = s.majorityElement([3,2,3])
    print(majorityElement)

# 2020.12.1
# 因为数组内一定有一个元素超过半数,所以只要排序之后输出一半位置的那个数(注释里的方法)
# Counter用来对数组中元素出现次数进行统计，然后通过most_common函数找到出现次数最多的元素。
# 这种方法对于数组就没有过多限制，甚至是各种类型元素混合的数组也可以