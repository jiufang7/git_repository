class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        deep = 0
        if not root:
            return deep
        else:
            deep = deep + 1
            if not root.left:
                return self.minDepth(root.right) + 1
            elif not root.right:
                return self.minDepth(root.left) + 1
            else:
                return min(self.minDepth(root.left), self.minDepth(root.right)) + 1

# 2020.10.15
# 判断二叉树的最小深度
# 和判断最大深度稍微有一点点不同，但是大致思路一致
# 区别在于，如果一个节点只有一侧有子树，那么它的最短深度就是自己子树的最短深度，不用两者比较取min