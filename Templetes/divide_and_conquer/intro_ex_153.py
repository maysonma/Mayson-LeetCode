from typing import List

"""
采用闭区间模式[l, r]
base case为 长度为1的情况
m = l + (r - l) // 2
递归调用为
find(l, m), find(m+1, r)
奇数分割情况为
0 1 2 | 3 4
偶数分割情况为
0 1 | 2 3
初始调用为
find(0, len(nums)-1)
"""


class Solution:
    def findMin(self, nums: List[int]) -> int:
        def find(nums, l, r):
            if nums[l] < nums[r]:
                return nums[l]
            if l + 1 >= r:
                return min(nums[l:r + 1])
            m = l + (r - l) // 2
            return min(find(nums, l, m - 1), find(nums, m, r))

        return find(nums, 0, len(nums) - 1)
