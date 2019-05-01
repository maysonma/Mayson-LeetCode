class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)
        MAXV = float('inf')
        MINV = -MAXV
        if n1 > n2:
            return self.findMedianSortedArrays(nums2, nums1)
        half = (n1 + n2 + 1) // 2

        # l = 0, r = n1+1
        def bin_search(l, r):
            while l < r:
                m = l + (r - l) // 2
                cut2 = half - m
                l1 = nums1[m - 1] if m > 0 else MINV
                r1 = nums1[m] if m < n1 else MAXV
                l2 = nums2[cut2 - 1] if cut2 > 0 else MINV
                r2 = nums2[cut2] if cut2 < n2 else MAXV
                if l1 > r2:
                    r = m
                elif l2 > r1:
                    l = m + 1
                else:
                    if (n1 + n2) % 2 == 0:
                        return float(max(l1, l2) + min(r1, r2)) / 2
                    else:
                        return max(l1, l2)

        return bin_search(0, n1 + 1)
