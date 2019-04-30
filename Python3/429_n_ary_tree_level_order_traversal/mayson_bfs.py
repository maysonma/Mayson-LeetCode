"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        def bfs(root):
            if root is None:
                return []
            cur = [root]
            nxt = []
            ans = []
            while cur:
                ans.append([node.val for node in cur])
                for node in cur:
                    for child in node.children:
                        nxt.append(child)
                cur = nxt
                nxt = []
            return ans

        return bfs(root)
