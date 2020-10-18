class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        deep = 0
        if not root:
            return deep
        else:
            deep = deep + 1
            return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

# 2020.10.15
# 递归求二叉树最大深度