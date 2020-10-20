class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int):
        if not root:
            return False
        stack = [root] #存放节点的栈
        while stack:
            p = stack.pop()
            if p.right:
                stack.append(p.right)
                p.right.val += p.val 
            if p.left:
                stack.append(p.left)
                p.left.val += p.val 
            if not p.left and not p.right:
                if p.val == sum:
                    return True
        return False

# 2020.10.20
# 用栈，一层层迭代
# 如果节点有孩子节点，就修改节点的值  改为父亲节点的值+自己的值
# 如果是叶子节点，根据上面的修改，此时它的值就是这条路径的值