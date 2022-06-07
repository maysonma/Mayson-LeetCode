# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Is this problem really HARD?
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = root.val

        def dfs(node):
            # return max sum including the curr node
            nonlocal max_sum
            if node is None:
                return 0

            sum_left = dfs(node.left)
            sum_right = dfs(node.right)
            curr_sum = max(sum_left, 0) + max(sum_right, 0) + node.val
            max_sum = max(curr_sum, max_sum)

            return max(sum_left, sum_right, 0) + node.val

        dfs(root)
        return max_sum
