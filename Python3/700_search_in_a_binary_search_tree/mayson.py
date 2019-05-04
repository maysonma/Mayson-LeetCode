# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        def search(root, val):
            if not root or root.val == val:
                return root
            if val < root.val:
                return search(root.left, val)
            else:
                return search(root.right, val)

        return search(root, val)
