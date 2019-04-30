# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        cur_min = float('inf')
        prev = None

        def in_order(node):
            nonlocal prev, cur_min
            if node is None:
                return
            in_order(node.left)
            if prev:
                cur_min = min(node.val - prev.val, cur_min)
            prev = node
            in_order(node.right)

        in_order(root)
        return cur_min
