# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def is_same(p, q):
            if p is None and q is None:
                return True
            elif p is None and q is not None:
                return False
            elif p is not None and q is None:
                return False
            elif p.val != q.val:
                return False
            else:
                return is_same(p.left, q.left) and is_same(p.right, q.right)

        return is_same(p, q)
