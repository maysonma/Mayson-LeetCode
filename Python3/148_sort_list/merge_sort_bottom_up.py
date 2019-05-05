# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        def merge(l1, l2):
            dummy = ListNode(0)
            tail = dummy
            while l1 and l2:
                if l1.val > l2.val:
                    l1, l2 = l2, l1
                tail.next = l1
                l1 = l1.next
                tail = tail.next
            if l1:
                tail.next = l1
            if l2:
                tail.next = l2
            while tail.next:
                tail = tail.next
            return dummy.next, tail

        def split(head, n):
            n = n - 1
            while head and n:
                head = head.next
                n -= 1
            if head:
                rest = head.next
                head.next = None
                return rest
            else:
                return None

        counter = 0
        dummy = ListNode(0)
        dummy.next = head
        while head:
            counter += 1
            head = head.next
        i = 1
        # log(n) iterations
        while i < counter:
            tail = dummy
            cur = dummy.next
            # O(n) iterations
            while cur:
                l = cur
                r = split(l, i)
                cur = split(r, i)
                h, t = merge(l, r)
                tail.next = h
                tail = t
            i *= 2
        return dummy.next
