class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def countNodes(self, root: TreeNode):
        if not root:
            return 0
        else:
            return self.countNodes(root.right) + self.countNodes(root.left) + 1

# 2020.10.21
# 虽然说是完全二叉树的个数，但是递归用数二叉树的节点个数也可以AC