# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        def dfs(node):
            if node.left is None and node.right is None:
                return 1
            if node.left is None:
                return dfs(node.right) + 1
            if node.right is None:
                return dfs(node.left) + 1
            else:
                return min(dfs(node.left), dfs(node.right)) + 1

        if root is None:
            return 0
        return dfs(root)
