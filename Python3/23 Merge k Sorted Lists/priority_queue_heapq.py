# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import heapq


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        ListNode.__lt__ = lambda self, other: self.val < other.val
        min_heap = []
        dummy = ListNode(0)
        tail = dummy
        for l in lists:
            if l:
                heapq.heappush(min_heap, (l.val, l))
        while min_heap:
            _, cur = heapq.heappop(min_heap)
            tail.next = cur
            tail = tail.next
            if cur.next:
                heapq.heappush(min_heap, (cur.next.val, cur.next))
        return dummy.next
