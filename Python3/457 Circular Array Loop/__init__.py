from typing import List


class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        def move(idx):
            nonlocal nums
            return (idx + nums[idx]) % len(nums)

        def detect_cycle(start):
            nonlocal nums
            if move(start) == start:
                return False
            curr = start
            sign = nums[start]
            while True:
                if nums[curr] * sign < 0:
                    return False
                curr = move(curr)
                if curr == start:
                    return True

        for start in range(len(nums)):
            slow = fast = start
            while True:
                fast = move(move(fast))
                slow = move(slow)
                if fast == slow:
                    break
            if detect_cycle(slow):
                return True

        return False
