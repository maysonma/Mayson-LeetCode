# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        def merge(l1, l2):
            if l1 is None:
                return l2
            elif l2 is None:
                return l1
            else:
                if l1.val <= l2.val:
                    l1.next = merge(l1.next, l2)
                    return l1
                else:
                    l2.next = merge(l1, l2.next)
                    return l2

        return merge(l1, l2)
