class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        def bin_search(l, r):
            while l != r:
                m = l + (r - l) // 2
                if A[m] > A[m + 1]:
                    r = m
                else:
                    l = m + 1
            return l

        return bin_search(0, len(A))
