# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        q = collections.deque()
        stack = [root]
        while stack:
            ptr = stack.pop()
            q.appendleft(ptr.val)
            if ptr.left is not None:
                stack.append(ptr.left)
            if ptr.right is not None:
                stack.append(ptr.right)
        return list(q)
