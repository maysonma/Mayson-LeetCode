from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary_search(move_forward=True):
            nonlocal nums, target
            start = 0
            end = len(nums) - 1
            key = -1
            while start <= end:
                mid = start + (end - start) // 2
                if target > nums[mid]:
                    start = mid + 1
                elif target < nums[mid]:
                    end = mid - 1
                else:
                    key = mid
                    if move_forward:
                        start = mid + 1
                    else:
                        end = mid - 1
            return key

        result = [-1, -1]
        result[0] = binary_search(False)
        if not result[0] == -1:
            result[1] = binary_search(True)
        return result
