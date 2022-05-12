# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None

        slow = fast = head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        if fast != slow:
            return None

        def cycle_len(start):
            count = 0
            curr = start
            while True:
                curr = curr.next
                count += 1
                if curr == start:
                    break
            return count

        n = cycle_len(slow)
        ptr1 = ptr2 = head
        for _ in range(n):
            ptr1 = ptr1.next

        while ptr1 != ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next

        return ptr1
