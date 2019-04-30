# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        leaves = []

        def pre_order(node):
            if node is None:
                return
            if node.left is None and node.right is None:
                leaves.append(node.val)
                return
            pre_order(node.left)
            pre_order(node.right)

        pre_order(root1)
        counter = -1

        def check(node):
            nonlocal counter
            if node is None:
                return True
            if node.left is None and node.right is None:
                counter += 1
                if counter >= len(leaves) or leaves[counter] != node.val:
                    return False
                else:
                    return True
            return check(node.left) and check(node.right)

        return check(root2)
