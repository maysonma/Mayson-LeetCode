# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        def dfs(node):
            if node is None:
                return True
            if node.val != root.val:
                return False
            l = dfs(node.left)
            r = dfs(node.right)
            return l and r

        if root is None:
            return True
        else:
            return dfs(root)
