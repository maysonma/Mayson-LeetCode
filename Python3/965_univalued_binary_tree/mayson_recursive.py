# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        def solve(root):
            if root.left is None and root.right is None:
                return root.val
            if root.left is None:
                r = solve(root.right)
                return root.val if root.val == r else -1
            if root.right is None:
                l = solve(root.left)
                return root.val if root.val == l else -1
            l = solve(root.left)
            r = solve(root.right)
            return root.val if root.val == l and root.val == r else -1

        if root is None:
            return True
        else:
            return False if solve(root) == -1 else True
