class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        elif p is not None and q is not None:
            if p.val == q.val:
                return self.isSameTree(p.right,q.right) and self.isSameTree(p.left, q.left)
            else:
                return False
        else:
            return False

# 2010.10.13
# 新电脑环境刚配好 以后尽量在实验室刷题吧
# 判断两棵树是否相同，很简单的递归，没什么好说的