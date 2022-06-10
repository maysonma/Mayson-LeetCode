from collections import deque
from typing import List

from collections import deque


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        queue = deque()
        queue.append([])
        result = []

        for num in nums:
            n = len(queue)
            for _ in range(n):
                old_permutation = queue.popleft()
                for j in range(len(old_permutation) + 1):
                    new_permutation = list(old_permutation)
                    new_permutation.insert(j, num)
                    if len(new_permutation) == len(nums):
                        result.append(new_permutation)
                    else:
                        queue.append(new_permutation)
        return result
