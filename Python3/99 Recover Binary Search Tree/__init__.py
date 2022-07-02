# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        first_node = None  # greater than its successor
        second_node = None  # smaller than its predecessor
        predecessor = TreeNode(float('-inf'))

        # In-order traversal
        def dfs(node):
            nonlocal first_node, second_node, predecessor
            if node is None:
                return
            dfs(node.left)

            if first_node is None and node.val < predecessor.val:
                first_node = predecessor
            if first_node is not None and node.val < predecessor.val:
                second_node = node
            predecessor = node

            dfs(node.right)

        dfs(root)
        first_node.val, second_node.val = second_node.val, first_node.val
