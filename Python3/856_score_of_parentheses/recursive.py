class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        # l = 0, r = len(S) - 1
        def score(S, l, r):
            # Case: '()'
            if l + 1 == r:
                return 1
            acc = 0
            for i in range(l, r):
                if S[i] == '(':
                    acc += 1
                else:
                    acc -= 1
                if acc == 0:
                    return score(S, l, i) + score(S, i + 1, r)
            return 2 * score(S, l + 1, r - 1)

        return score(S, 0, len(S) - 1)
