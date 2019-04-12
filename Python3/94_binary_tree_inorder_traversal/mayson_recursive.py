# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []

        def in_order(root):
            nonlocal ans
            if root is None:
                return
            in_order(root.left)
            ans.append(root.val)
            in_order(root.right)

        in_order(root)
        return ans
