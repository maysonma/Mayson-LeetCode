from collections import deque
from typing import List


# class Solution:
#     def letterCasePermutation(self, s: str) -> List[str]:
#         ans = []
#         queue = deque()
#         queue.append([])
#         for char in s:
#             n = len(queue)
#             for _ in range(n):
#                 old_permutation = queue.popleft()
#                 if char.isdigit():
#                     new_permutation = old_permutation
#                     new_permutation.append(char)
#                     if len(new_permutation) == len(s):
#                         ans.append(''.join(new_permutation))
#                     else:
#                         queue.append(new_permutation)
#                 else:
#                     new_permutation_l = old_permutation
#                     new_permutation_u = list(old_permutation)
#                     new_permutation_l.append(char.lower())
#                     new_permutation_u.append(char.upper())
#                     if len(new_permutation_l) == len(s):
#                         ans.append(''.join(new_permutation_l))
#                         ans.append(''.join(new_permutation_u))
#                     else:
#                         queue.append(new_permutation_l)
#                         queue.append(new_permutation_u)
#         return ans


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = [s]
        for i in range(len(s)):
            if s[i].isalpha():
                n = len(ans)
                for j in range(n):
                    ans.append(ans[j][:i] + ans[j][i].swapcase() + ans[j][i + 1:])
        return ans
