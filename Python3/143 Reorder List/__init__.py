# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(str(temp.val) + " ", end='')
            temp = temp.next
        print()


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None:
            return head

        def find_middle(head):
            fast = slow = head
            while fast is not None and fast.next is not None:
                fast = fast.next.next
                slow = slow.next
            return slow

        def reverse_ll(head):
            if head.next is None:
                return head
            prev = head
            curr = head.next
            head.next = None
            while curr is not None:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev

        mid = find_middle(head)
        rev_head = reverse_ll(mid)

        ptr1 = head
        ptr2 = rev_head

        while ptr1 != mid:
            temp = ptr1.next
            ptr1.next = ptr2
            ptr2 = ptr2.next
            ptr1.next.next = temp
            ptr1 = temp

        mid.next = None


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    # head.next.next.next.next = ListNode(10)
    # head.next.next.next.next.next = ListNode(12)
    s = Solution()
    s.reorderList(head)
    # head.print_list()
