# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        def insert(root, val):
            if not root:
                return TreeNode(val)
            if val <= root.val:
                root.left = insert(root.left, val)
                return root
            else:
                root.right = insert(root.right, val)
                return root

        return insert(root, val)
