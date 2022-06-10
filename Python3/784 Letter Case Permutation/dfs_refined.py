class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        def search(S, m, n, curr, ans):
            if m == n:
                ans.append(''.join(curr))
                return
            curr.append(S[m])
            search(S, m + 1, n, curr, ans)
            curr.pop()
            if S[m].isalpha():
                curr.append(chr(ord(S[m]) ^ (1 << 5)))
                search(S, m + 1, n, curr, ans)
                curr.pop()

        ans = []
        search(S, 0, len(S), [], ans)
        return ans
