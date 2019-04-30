# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False
        slow = fast = head
        while True:
            if fast.next is None or fast.next.next is None:
                return False
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
