class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) :
        if not root:
            return []
        ans = []
        queue = [root]
        tag = False
        while queue:
            temp = []
            l = len(queue)
            for i in range(l):
                node = queue.pop(0) # 取出队列中的第一个元素
                #temp.append(node.val)
                if tag:
                    temp.insert(0, node.val) # 添加在列表头用insert加索引的方法
                else:
                    temp.append(node.val) # append方法只能添加在列表末端

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(temp)
            if tag:
                tag = False
            else:
                tag = True
        return ans

# 2020.10.17
# 锯齿形层序遍历，在层序遍历的基础上，每一层判断奇偶
# 奇数添加在列表尾部，偶数添加在列表头部
# 每次从列表中取元素，都是从头部开始
