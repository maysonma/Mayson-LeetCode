# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        def bfs(root):
            if root is None:
                return []
            cur = [root]
            nxt = []
            ans = []
            while cur:
                ans.append([node.val for node in cur])
                for node in cur:
                    if node.left:
                        nxt.append(node.left)
                    if node.right:
                        nxt.append(node.right)
                cur = nxt
                nxt = []
            return ans

        return list(reversed(bfs(root)))
