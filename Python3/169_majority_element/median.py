import statistics
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return int(statistics.median(nums))
