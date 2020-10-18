# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        re = ListNode(0)
        r = re
        if l1 == None:
            return l2
        elif l2 == None :
            return l1
        else:
            while(l1 or l2):
                x = l1.val if l1 else 0
                y = l2.val if l2 else 0
                # 如果l1/l2非空则 x = l1/l2.val,不然 x = 0
                res = x + y + carry
                carry = res // 10
                # " / "表示浮点数除法，返回浮点结果;" // "表示整数除法
                r.next = ListNode(res % 10)
                r = r.next
                if l1 != None:
                    l1 = l1.next
                if l2 != None:
                    l2 = l2.next
            if carry != 0:
                r.next = ListNode(1)
            return re.next
            # re.val是0 结果是从re.next开始的
    

# 2020.6.17