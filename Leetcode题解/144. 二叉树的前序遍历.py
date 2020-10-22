class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) :
        '''
        递归的做法
        result = []
        def travel(node: TreeNode):
            nonlocal result
            if node:
                result.append(node.val)
                travel(node.left)
                travel(node.right)
        travel(root)
        return result
        '''
        if not root:
            return []
        
        stack = [root]
        res = []
        while stack:
            cur = stack.pop()
            res.append(cur.val)            
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
        return res

# 2020.10.22
# 二叉树的前序遍历 两种方法  递归和迭代     
        