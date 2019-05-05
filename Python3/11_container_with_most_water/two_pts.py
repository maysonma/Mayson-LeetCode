class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        cur_max = 0
        while l != r:
            h = min(height[l], height[r])
            volume = h * (r - l)
            cur_max = max(cur_max, volume)
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return cur_max
