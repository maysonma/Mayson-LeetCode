# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        tree_diameter = 0

        def dfs(node):
            # return the height
            nonlocal tree_diameter

            if node is None:
                return 0

            lh = dfs(node.left)
            rh = dfs(node.right)

            diameter = lh + rh

            if node.left or node.right:
                if node.left:
                    diameter += 1
                if node.right:
                    diameter += 1
                tree_diameter = max(tree_diameter, diameter)
                return max(lh, rh) + 1
            else:
                return 0

        dfs(root)
        return tree_diameter
