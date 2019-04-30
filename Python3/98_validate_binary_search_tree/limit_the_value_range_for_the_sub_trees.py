# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def is_valid(node, min_node, max_node):
            if node is None:
                return True
            if min_node and node.val <= min_node.val or max_node and node.val >= max_node.val:
                return False
            return is_valid(node.left, min_node, node) and is_valid(node.right, node, max_node)

        return is_valid(root, None, None)
