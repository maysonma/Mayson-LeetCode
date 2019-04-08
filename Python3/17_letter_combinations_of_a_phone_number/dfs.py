from typing import *


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        n = len(digits)
        digit_char_arr = [{'a', 'b', 'c'},
                          {'d', 'e', 'f'},
                          {'g', 'h', 'i'},
                          {'j', 'k', 'l'},
                          {'m', 'n', 'o'},
                          {'p', 'q', 'r', 's'},
                          {'t', 'u', 'v'},
                          {'w', 'x', 'y', 'z'}]
        ans = []
        stack = []

        def dfs():
            nonlocal n, digits, digit_char_arr, ans, stack
            m = len(stack)
            if m == n:
                ans.append(''.join(stack))
                return
            for char in digit_char_arr[ord(digits[m]) - ord('2')]:
                stack.append(char)
                dfs()
                stack.pop()

        dfs()
        # return sorted(ans)
        return ans
