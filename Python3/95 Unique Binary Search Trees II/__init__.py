# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from itertools import product
from copy import deepcopy


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        mem = {}

        def gt_rec(i, j):
            ans = []
            if i >= j:
                ans.append(None)
            else:
                for k in range(i, j):
                    left = gt_rec(i, k)
                    right = gt_rec(k + 1, j)
                    for l, r in product(left, right):
                        root = TreeNode(k)
                        root.left = l
                        root.right = r
                        ans.append(root)
            mem[(i, j)] = ans
            return ans

        return gt_rec(1, n + 1)
