# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from heapq import *
from typing import List, Optional


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        for i in range(len(lists)):
            l = lists[i]
            if l is not None:
                min_heap.append((l.val, i))
        heapify(min_heap)
        cur = head = ListNode()
        while min_heap:
            _, idx = heappop(min_heap)
            node = lists[idx]
            cur.next = node
            cur = cur.next
            if node.next is not None:
                lists[idx] = node.next
                heappush(min_heap, (node.next.val, idx))
        return head.next
