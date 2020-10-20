class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int):
        ans = []
        if not root:
            return ans

        def dfs(root, temp):
            res = 0
            if root.right:
                dfs(root.right, temp + [root.right.val])  # temp + [] 就是把后面的列表元素添加到temp中
            if root.left:
                dfs(root.left, temp + [root.left.val])
            if not root.right and not root.left:
                for i in temp:
                    res += i
                if res == sum:
                    ans.append(temp)
    
        dfs(root, [root.val])
        return ans

# 2020.10.20
# 这次就不用上一题一样的栈了，用了dfs深度优先搜索