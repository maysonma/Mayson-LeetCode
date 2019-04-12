# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        ans = []
        stack = []
        last = None
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                node = stack[-1]
                if node.right is None or node.right == last:
                    ans.append(node.val)
                    last = node
                    stack.pop()
                else:
                    root = node.right
        return ans
