# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def is_sym(p, q):
            if p is None and q is None:
                return True
            if p is None or q is None:
                return False
            else:
                return p.val == q.val and is_sym(p.left, q.right) and is_sym(p.right, q.left)

        if root is None:
            return True
        return is_sym(root.left, root.right)
