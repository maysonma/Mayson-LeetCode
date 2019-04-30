# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        prev_ = None

        def in_order(node):
            nonlocal prev_
            if node is None:
                return True
            if not in_order(node.left):
                return False
            if prev_ and node.val <= prev_.val:
                return False
            prev_ = node
            return in_order(node.right)

        return in_order(root)
