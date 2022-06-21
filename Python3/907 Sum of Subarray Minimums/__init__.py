from typing import List


class Solution:
    # monotonic stack
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        left = [-1] * n
        right = [n] * n
        in_stack = []
        for i in range(n):
            num = arr[i]
            while in_stack and arr[in_stack[-1]] > num:
                x = in_stack.pop()
                right[x] = i  # next less element
            if in_stack:
                left[i] = in_stack[-1]  # previous less element
            in_stack.append(i)

        ans = 0
        for i in range(n):
            ans += (i - left[i]) * (right[i] - i) * arr[i]

        return ans % int(1e9 + 7)
