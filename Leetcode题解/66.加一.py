class Solution:
    def plusOne(self, digits):
        carry = 1 
        # 指示物carry,从列表末尾开始每个元素都加指示物
        # 如果不用进位指示物就改为0，如果需要进位元素修改为0，指示物还是1
        for i in reversed(range(0,len(digits))):
            digits[i] = digits[i] + carry
            if digits[i] == 10:
                digits[i] = 0
                carry = 1
            else:
                carry = 0
            
        if digits[0] == 0:
            # 如果是类似于[9,9],现在到这里已经变成了[0,0],所以在列表头上插入1
            digits.insert(0, 1)
            return digits
        else:
            return digits

if __name__ == '__main__':
    s = Solution()
    plus_one = s.plusOne([9,9,9])
    print(plus_one)

# 2020.6.11
# list.append()的添加方法只能添加在列表的末尾
# list.insert(index,添加内容)的方法可以在指定的index位置上添加元素
# [1]+[2,3] 结果是[1,2,3]  这也是一种列表合并的办法 
