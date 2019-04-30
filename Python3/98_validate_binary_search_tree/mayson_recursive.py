# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def search(root):
            if root.left is None and root.right is None:
                return root.val, root.val, True
            if root.left is None:
                # root.right is not None
                r_min, r_max, r_valid = search(root.right)
                return root.val, r_max, r_valid and root.val < r_min
            if root.right is None:
                # root.left is not None
                l_min, l_max, l_valid = search(root.left)
                return l_min, root.val, l_valid and root.val > l_max
            l_min, l_max, l_valid = search(root.left)
            r_min, r_max, r_valid = search(root.right)
            return min(l_min, r_min), max(l_max, r_max), l_valid and r_valid and root.val > l_max and root.val < r_min

        if root is None:
            return True
        return search(root)[2]
