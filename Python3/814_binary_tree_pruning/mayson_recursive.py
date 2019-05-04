# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        # False = not containing a 1
        def prune(root):
            if root is None:
                return False
            l = prune(root.left)
            r = prune(root.right)
            if not l:
                root.left = None
            if not r:
                root.right = None
            if not l and not r and root.val != 1:
                return False
            else:
                return True

        prune(root)
        return root if prune(root) else None
