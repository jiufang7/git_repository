class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return None
        
        x = preorder.pop(0) #移除前序中第一个结点，它作为根结点
        node = TreeNode(x)
        i = inorder.index(x)

        node.left = self.buildTree(preorder[:i], inorder[:i])
        node.right = self.buildTree(preorder[i:],inorder[i+1: ])
        # 以前序[3,9,20,15,7] 中序[9,3,15,20,7]举例
        # 取出前序的3作为根结点,前序列表变为[9,20,15,7]
        # 3在中序里的索引是1
        # 前序列表[:i]这里是[9]，中序列表[:i]是[9]，代表左子树结点，可以继续递归
        # 前序列表[i:]这里是[20,15,7],中序列表[i+1:] 是[15,20,7]，代表右子树结点，可以继续递归
        return node

# 2020.10.18
# 前序遍历[根结点，左子树结点，右子树结点]
# 中序遍历[左子树结点，根结点，右子树结点]
# 在取出根结点之后，对于剩下部分，就可以按照左右子树的情况，递归解决。