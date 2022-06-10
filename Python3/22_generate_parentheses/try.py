from collections import deque
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        queue = deque()
        queue.append(([], 0, 0))  # (comb, open, close)
        ans = []
        for i in range(2 * n):
            m = len(queue)
            for _ in range(m):
                old = queue.popleft()
                if n - old[1] > 0:  # can add '('
                    new_comb = list(old[0])
                    new_comb.append('(')
                    queue.append((new_comb, old[1] + 1, old[2]))
                if old[1] - old[2] > 0:  # can add ')'
                    new_comb = old[0]
                    new_comb.append(')')
                    if len(new_comb) == 2 * n:
                        ans.append(''.join(new_comb))
                    else:
                        queue.append((new_comb, old[1], old[2] + 1))
        return ans
