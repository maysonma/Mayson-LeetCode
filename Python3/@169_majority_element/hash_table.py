from collections import defaultdict


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = defaultdict(int)
        thed = len(nums) // 2
        for num in nums:
            dic[num] += 1
            if dic[num] > thed:
                return num
        return -1
