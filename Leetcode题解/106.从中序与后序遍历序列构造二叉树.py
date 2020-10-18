class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder, postorder):
        """
        :type postorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not postorder:
            return None
        
        x = postorder.pop() #移除后序中最后一个结点，它作为根结点
        node = TreeNode(x)
        i = inorder.index(x)

        node.left = self.buildTree(inorder[:i], postorder[:i] )
        node.right = self.buildTree(inorder[i+1:], postorder[i:])
        # 以后序[9,15,7,20,3] 中序[9,3,15,20,7]举例
        # 取出后序的3作为根结点,后序列表变为[9,15,7,20]
        # 3在中序里的索引是1
        # 后序列表[:i]这里是[9]，中序列表[:i]是[9]，代表左子树结点，可以继续递归
        # 后序列表[i:]这里是[15,7,20],中序列表[i+1:] 是[15,20,7]，代表右子树结点，可以继续递归
        return node

# 2020.10.18