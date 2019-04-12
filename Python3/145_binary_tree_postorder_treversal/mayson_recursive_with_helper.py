# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        def helper(node):
            nonlocal ans
            if node is None:
                return
            helper(node.left)
            helper(node.right)
            ans.append(node.val)
        helper(root)
        return ans