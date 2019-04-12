"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        stack = [root]
        ans = []
        while stack:
            root = stack.pop()
            ans.append(root.val)
            for child in root.children[::-1]:
                stack.append(child)
        return ans
