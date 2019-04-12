"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
from collections import deque
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        ans = deque()
        stack = [root]
        while stack:
            root = stack.pop()
            ans.appendleft(root.val)
            for child in root.children:
                stack.append(child)
        return list(ans)