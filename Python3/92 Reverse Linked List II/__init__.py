# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right or head is None:
            return head

        i = 1
        pre, cur = None, head
        while cur is not None and i < left:
            pre = cur
            cur = cur.next
            i += 1

        last_of_first_part = pre
        end_of_sub_list = cur
        pre = None

        nxt = None
        while cur is not None and i <= right:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
            i += 1

        if last_of_first_part is not None:
            last_of_first_part.next = pre
        else:
            head = pre

        end_of_sub_list.next = cur

        return head
