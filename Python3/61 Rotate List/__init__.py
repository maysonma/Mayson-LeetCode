# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or k <= 0:
            return head

        last_node_of_list = head
        list_len = 1
        while last_node_of_list.next is not None:
            last_node_of_list = last_node_of_list.next
            list_len += 1

        rotation = k % list_len
        last_node_of_list.next = head

        i = 0
        cur = head
        while i < list_len - rotation - 1:
            cur = cur.next
            i += 1

        head = cur.next
        cur.next = None
        return head
