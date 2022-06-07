# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidSequence(self, root: Optional[TreeNode], arr: List[int]) -> bool:
        def dfs(root, depth=0):
            nonlocal arr
            if root is None:
                return False

            if depth >= len(arr) or arr[depth] != root.val:
                return False

            if root.left is None and root.right is None and depth == len(arr) - 1:
                return True

            return dfs(root.left, depth + 1) or dfs(root.right, depth + 1)

        return dfs(root)
