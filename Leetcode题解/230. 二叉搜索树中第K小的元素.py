class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) :
        ans = [] #存放结果的列表
        queue = [root] # 层序时候用的队列
        while queue:
            l = len(queue)
            for i in range(l):
                node = queue.pop(0) # 取出队列中的第一个元素-
                ans.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        ans.sort()
        return ans[k-1]

# 2020.10.22
# 搜索二叉树第K小的节点
# 正常来说的话，应该是用中序遍历，这样结果都是按照顺序排列的，然后取第k个
# 代码这里用的是层序遍历，所以最后又sort排序了一下