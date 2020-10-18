# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode):
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False

# 2020.10.9
# 停摆了很久之后又开始的刷题计划
# 判断链表里的环，非常简单，快慢两节点是否相遇
