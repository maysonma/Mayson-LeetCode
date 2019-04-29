class Solution:
    def mySqrt(self, x: int) -> int:
        def bin_search(target, l, r):
            while l != r:
                m = l + (r - l) // 2
                if m * m > target:
                    r = m
                else:
                    l = m + 1
            return l

        return bin_search(x, 0, x + 1) - 1
