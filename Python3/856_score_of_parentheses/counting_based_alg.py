class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        acc = -1
        ans = 0
        for idx, ch in enumerate(S[:-1]):
            acc += 1 if ch == '(' else -1
            if S[idx] == '(' and S[idx + 1] == ')':
                ans += 2 ** acc
        return ans
