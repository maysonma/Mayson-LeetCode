# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from __future__ import print_function

from typing import Optional


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next
        print()


class Solution:
    def reverseKGroup(self, head: Optional[Node], k: int) -> Optional[Node]:
        def reverse_first_k(head, k):
            pre, cur = None, head
            i = 1
            while cur is not None and i <= k:
                pre = cur
                cur = cur.next
                i += 1
            if i <= k:
                return head, None

            i = 1
            pre, cur, nxt = None, head, None
            while i <= k:
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt
                i += 1

            head.next = cur
            return pre, head

        end_of_finished_part = None
        start_of_remain_part = head
        while start_of_remain_part is not None:
            new_head, end_of_reversed_part = reverse_first_k(start_of_remain_part, k)
            if end_of_finished_part is None:
                head = new_head
            else:
                end_of_finished_part.next = new_head
            if end_of_reversed_part is None:
                break
            end_of_finished_part = end_of_reversed_part
            start_of_remain_part = end_of_finished_part.next

        return head


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = Node(7)
    head.next.next.next.next.next.next.next = Node(8)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    sol = Solution()
    result = sol.reverseKGroup(head, 3)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()


main()
