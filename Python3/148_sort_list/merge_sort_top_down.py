# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        def sort_list(head):
            if not head or not head.next:
                return head
            slow = head
            fast = head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            right = slow.next
            slow.next = None
            head = sort_list(head)
            right = sort_list(right)
            return merge(head, right)

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
            return dummy.next

        return sort_list(head)
