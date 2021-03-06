class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) :
        if not root:
            return []
        ans = [] #存放结果的列表
        queue = [root] # 层序时候用的队列
        while queue:
            temp = [] # 当前层的队列
            l = len(queue)
            for i in range(l):
                node = queue.pop(0) # 取出队列中的第一个元素-
                temp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(temp)
        return ans

# 2020.10.17
# 二叉树的层序遍历，用队列来做