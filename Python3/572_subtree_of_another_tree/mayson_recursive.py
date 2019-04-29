class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def is_same(s, t):
            if s is None and t is None:
                return True
            if s is None or t is None:
                return False
            l = is_same(s.left, t.left)
            r = is_same(s.right, t.right)
            return l and r and s.val == t.val

        def solve(s, t):
            if s is None and t is None:
                return True
            if s is None:
                return False
            if t is None:
                return True
            if is_same(s, t):
                return True
            l = solve(s.left, t)
            r = solve(s.right, t)
            return l or r

        return solve(s, t)
