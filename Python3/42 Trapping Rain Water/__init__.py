from typing import List


# Two pointers
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left, right = 0, n - 1
        max_height_left, max_height_right = height[0], height[n - 1]
        ans = 0
        while left < right:
            if max_height_left <= max_height_right:
                ans += max_height_left - height[left]
                left += 1
                max_height_left = max(max_height_left, height[left])
            else:
                ans += max_height_right - height[right]
                right -= 1
                max_height_right = max(max_height_right, height[right])
        return ans
