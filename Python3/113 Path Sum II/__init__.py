# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        all_paths = []
        cur_path = deque()

        def dfs(root, sum):
            nonlocal all_paths, cur_path
            if root is None:
                return
            cur_path.append(root.val)
            if root.val == sum and root.left is None and root.right is None:
                all_paths.append(list(cur_path))

            dfs(root.left, sum - root.val)
            dfs(root.right, sum - root.val)

            cur_path.pop()

        dfs(root, targetSum)
        return all_paths


if __name__ == "__main__":
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    sum = 23
    sol = Solution()
    print("Tree paths with sum " + str(sum) +
          ": " + str(sol.pathSum(root, sum)))
