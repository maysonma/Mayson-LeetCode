class Solution:
    def numTrees(self, n: int) -> int:
        mem = {0: 1, 1: 1}

        def num_tree_rec(k):
            nonlocal mem
            if k in mem:
                return mem[k]

            ans = 0
            for i in range(k):
                left = num_tree_rec(i)
                right = num_tree_rec(k - i - 1)
                ans += left * right

            mem[k] = ans
            return ans

        return num_tree_rec(n)
