from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        for num in nums:
            current_level = len(ans)
            for i in range(current_level):
                ss = list(ans[i])
                ss.append(num)
                ans.append(ss)
        return ans
