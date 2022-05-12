# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def find_middle(head):
            fast = slow = head
            while fast is not None and fast.next is not None:
                fast = fast.next.next
                slow = slow.next
            return slow

        def reverse_ll(head):
            if head.next is None:
                return head
            p1 = head
            p2 = head.next
            head.next = None
            while p2 is not None:
                temp = p2.next
                p2.next = p1
                p1 = p2
                p2 = temp
            return p1

        mid = find_middle(head)
        r_head = reverse_ll(mid)

        left = head
        right = r_head

        palindrome = True
        while left is not None and left != mid:
            if left.val != right.val:
                palindrome = False
                break
            left = left.next
            right = right.next

        reverse_ll(mid)
        return palindrome
