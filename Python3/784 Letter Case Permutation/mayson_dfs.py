from typing import List


class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        def is_lower_case(char):
            return ord(char) >= ord('a') and ord(char) <= ord('z')

        def is_upper_case(char):
            return ord(char) >= ord('A') and ord(char) <= ord('Z')

        def search(S, m, n, curr, ans):
            if m == n:
                ans.append(''.join(curr))
                return
            if is_lower_case(S[m]):
                curr.append(S[m])
                search(S, m + 1, n, curr, ans)
                curr.pop()
                curr.append(S[m].upper())
                search(S, m + 1, n, curr, ans)
                curr.pop()
            elif is_upper_case(S[m]):
                curr.append(S[m])
                search(S, m + 1, n, curr, ans)
                curr.pop()
                curr.append(S[m].lower())
                search(S, m + 1, n, curr, ans)
                curr.pop()
            else:
                curr.append(S[m])
                search(S, m + 1, n, curr, ans)
                curr.pop()

        ans = []
        search(S, 0, len(S), [], ans)
        return ans
