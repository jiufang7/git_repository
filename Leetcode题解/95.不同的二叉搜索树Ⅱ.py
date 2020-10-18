# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        res = []
        if n < 1:
            return res
        else:
            return self.generateBST(1, n)
        
    def generateBST(self, start, end):
        res = []
        if start > end:
            res.append(None)
            return res
        else:
            for i in range(start, end + 1):
                # 左子树
                left_tree = self.generateBST(start, i - 1)
                # 右子树
                right_tree = self.generateBST(i + 1, end)
                for left in left_tree:
                    for right in right_tree:
                        root = TreeNode(i)
                        root.left = left
                        root.right = right
                        res.append(root)
            return res

# 2020.10.14
# 递归。

# 如果将 i 作为跟节点，那么 [1, i) 为 i 的左子树节点，(i, n] 为右子树节点。

# 问题就被拆分为两个子问题了：

# 求左子树的所有排列
# 求右子树的所有排列