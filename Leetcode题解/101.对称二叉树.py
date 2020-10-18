class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:

        def check(node1, node2):
            if not node1  and not node2 :
                return True
            elif not node1 or not node2:
                return False
            else:
                if node1.val != node2.val:
                    return False
                else:
                    return check(node1.left, node2.right) and check(node1.right, node2.left)

        return check(root, root)
        



# 2020.10.15
# 二叉树镜像对称，第一个反应是中序遍历是个回文
# 后来发现不对，单纯的中序遍历的话，还要考虑左右子树的深度一样才可以
# 最后用的递归 检查对称两个节点左右子树是否镜像对称