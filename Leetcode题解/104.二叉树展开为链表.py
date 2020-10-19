class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: TreeNode) :
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        if not root.left and not root.right:
            return root

        self.flatten(root.left)
        self.flatten(root.right)

        ltree, rtree = root.left, root.right
        root.right = ltree
        root.left = None

        p = root
        while p.right:
            p = p.right
        p.right = rtree
        