"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        ans = [root.val]
        for child in reversed(root.children):
            ans.extend(self.postorder(child)[::-1])
        return ans[::-1]
