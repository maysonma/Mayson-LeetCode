"""
@ Author: Hua Hua
# Definition of a binary tree node
# Binary search tree
# Balanced binary tree
# Binary tree traversal
# Binary tree traversal
    # Pre-order/In-order/Post-order
# How to create a BST
# Key to tree problems: recursion
# Time complexity: O(n) Space complexity: O(h)
----------------------------------------------------------------
Binary search tree: vals of left-subtree <= root.val < vals of right-subtree
----------------------------------------------------------------
Balanced Tree: the difference of the height of left/right subtrees is at most 1
----------------------------------------------------------------
# Important property: for a BST, in-order vals are sorted
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def create_bst(nums):
    root = None
    for num in nums:
        root = insert(root, num)
    return root


def insert(root, val):
    if root is None:
        return TreeNode(val)
    if val <= root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root

