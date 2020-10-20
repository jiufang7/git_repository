class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode): 
        if not root:
            return 0
        stack = [root] #存放节点的栈
        res = 0
        while stack:
            p = stack.pop()
            if p.right:
                stack.append(p.right)
                p.right.val += p.val * 10
            if p.left:
                stack.append(p.left)
                p.left.val += p.val * 10
            if not p.left and not p.right:
                res += p.val
        return res

# 2020.10.20
# 如果有孩子节点，那么就把孩子节点的值进行修改 父节点值*10+本身的值
# 如果是叶子节点，此时它的值就是根节点到叶子节点的数字