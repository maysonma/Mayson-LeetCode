"""
# Definition for a Node.
"""


class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None:
            return None
        cur = head
        while cur:
            dup = Node(cur.val, cur.next, None)
            cur.next = dup
            cur = dup.next
        cur = head
        while cur:
            cur.next.random = cur.random.next if cur.random else None
            cur = cur.next.next
        cur = head
        dummy = Node(0, cur.next, None)
        dup_cur = dummy
        while cur is not None:
            dup_cur.next = cur.next
            dup_cur = dup_cur.next
            cur.next = dup_cur.next
            cur = cur.next

        return dummy.next
