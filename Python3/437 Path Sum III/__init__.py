# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        cur_path = deque()

        def dfs(root):
            nonlocal cur_path, targetSum
            if root is None:
                return 0

            cur_path.append(root.val)
            sum = count = 0
            for v in reversed(cur_path):
                sum += v
                if sum == targetSum:
                    count += 1

            count += dfs(root.left) + dfs(root.right)
            cur_path.pop()
            return count

        return dfs(root)
