from typing import List


class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i = j = 0
        start = 0
        end = 1
        ans = []
        while i < len(firstList) and j < len(secondList):
            ia = firstList[i]
            ib = secondList[j]
            if ib[start] <= ia[end] <= ib[end] or ia[start] <= ib[end] <= ia[end]:  # overlap
                ans.append([max(ia[start], ib[start]), min(ia[end], ib[end])])
            if ia[end] < ib[end]:
                i += 1
            elif ib[end] < ia[end]:
                j += 1
            else:
                i += 1
                j += 1
        return ans
