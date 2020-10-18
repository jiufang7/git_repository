class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        def travel(node: TreeNode):
            nonlocal result
            if node != None:
                travel(node.left)
                result.append(node.val)
                travel(node.right)
        travel(root)
        return result

# 2020.10.9
# 二叉树的中序遍历 用的递归  没什么好说的
# 要明确 nonlocal 关键字是定义在闭包里面的
'''
x = 0
def outer():
	x = 1
	def inner():
		nonlocal x
		x = 2
		print("inner:", x)

	inner()
	print("outer:", x)

outer()
print("global:", x)

inner: 2
outer: 2
global: 0
'''